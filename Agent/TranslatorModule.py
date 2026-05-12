import torch
from transformers import pipeline,AutoModelForSeq2SeqLM, AutoTokenizer
#libs for measuring performance
import time
import psutil
import os

class Translator:
    def __init__(self, model_index=1):
        self.nllb_models = [
            "facebook/nllb-200-distilled-600M", 
            "facebook/mbart-large-50-many-to-many-mmt"
        ]
        self.model_number = model_index
        self.model_name = self.nllb_models[self.model_number]

        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        print(f"Loading {self.model_name} onto {self.device}...")
        
        # Load Language Detection Model
        #device parameter is for loading the language identification into the GPU
        self.lid_model = pipeline("text-classification", model="papluca/xlm-roberta-base-language-detection", device=0 if self.device == "cuda" else -1)
        
        # Load Translation Model and Tokenizer ONCE
        if self.model_number == 0:
            self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
            self.model = AutoModelForSeq2SeqLM.from_pretrained(self.model_name, 
                                                               #torch_dtype="auto"
                                                               torch_dtype=torch.float16,
                                                               offload_folder="offload",
                                                               attn_implementation="sdpa", 
                                                               device_map="auto")
        else:
            self.tokenizer = AutoTokenizer.from_pretrained(self.model_name, use_fast=False)
            self.model = AutoModelForSeq2SeqLM.from_pretrained(self.model_name, torch_dtype=torch.float16, device_map="auto")

        self.lang_mapping = {
            "ar": "arb_Arab", "fa": "pes_Arab", "de": "deu_Latn", "el": "ell_Grek",
            "it": "ita_Latn", "es": "spa_Latn", "ca": "cat_Latn", "prs": "prs_Arab",
            "fr": "fra_Latn", "en": "eng_Latn", "la": "lat_Latn"
        }

        self.lang_mapping_bart = {
            "ar":  "ar_AR", "fa": "fa_IR", "de": "de_DE", "el": "el_GR", #I think greek is not supported in my current version
            "it":  "it_IT", "es": "es_XX", "ca": "ca_ES", "fr": "fr_XX",
            "en":  "en_XX", "la": "en_XX", "ur": "ur_PK", "prs": "fa_IR"
        }

    def detect_language(self, text: str):
        detection = self.lid_model(text)[0]
        return detection['label']

    def translate(self, text: str, language_input_code: str = "en", language_output_code: str = "fr"):
        if not text.strip():
            return "WARNING: You need to input some text to translate"

        start = time.perf_counter()
        
        # Logic for language codes
        if self.model_number == 0:
            src_lang = self.lang_mapping.get(language_input_code, "eng_Latn")
            tgt_lang = self.lang_mapping.get(language_output_code, "fra_Latn")
            self.tokenizer.src_lang = src_lang
            forced_id = self.tokenizer.convert_tokens_to_ids(tgt_lang)
        else:
            # mBART specific formatting
            src_lang = self.lang_mapping_bart.get(language_input_code, "en_XX")
            tgt_lang = self.lang_mapping_bart.get(language_output_code, "en_XX")
            self.tokenizer.src_lang = src_lang
            forced_id = self.tokenizer.lang_code_to_id[tgt_lang]
        
        # 3. Add truncation and move inputs to GPU
        inputs = self.tokenizer(text, return_tensors="pt", truncation=True, max_length=512).to(self.device)

        translated_tokens = self.model.generate(
            **inputs, 
            forced_bos_token_id=forced_id, 
            max_length=512,
            # --- SPEED OPTIMIZATIONS ---
            do_sample=False,      # Disables random sampling (faster)
            num_beams=1,         # Switches from Beam Search to Greedy Search (MUCH faster)
            early_stopping=True  # Stops immediately when the end-token is found
        )
        
        end = time.perf_counter()
        
        # Performance metrics
        process = psutil.Process(os.getpid())
        cpu = process.cpu_percent(interval=None) # interval=None is better for repeated calls
        ram_mb = process.memory_info().rss / (1024 ** 2)

        print(f"--- Stats ({self.model_name}) ---")
        print(f"RAM: {ram_mb:.2f} MB | Time: {end - start:.4f}s")

        return self.tokenizer.batch_decode(translated_tokens, skip_special_tokens=True)[0]
    
