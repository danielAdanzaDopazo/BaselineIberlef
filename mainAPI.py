import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
from fastapi import FastAPI
from Agent.TranslatorModule import Translator
from LLMMaganer.Executor import TriggerLLMOllama
from LLMMaganer.RAGmodule import GenerateSimplifierPrompt
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from typing import Union, List
import time
from NLPModule import smart_chunking

class SimplifierRequest(BaseModel):
    text: Union[str, List[str]]
    languageInput: str = ""

class TranslationRequest(BaseModel):
    text: Union[str, List[str]]
    languageOutput: str = "en"


app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

translator_model = Translator(model_index=0)

@app.post("/translator")
def translator(request: TranslationRequest):

    #retrieving list of text
    is_list = isinstance(request.text, list)
    texts_to_process = request.text if is_list else [request.text]

    if not texts_to_process or (not is_list and request.text == ""):
        texts_to_process = ["This is a sample text to help with some translations"]

    results = []

    for textString in texts_to_process:

        languageInput = translator_model.detect_language(textString)

        #paragraphs = [p for p in textString.split('\n\n') if p.strip()]
        paragraphs = smart_chunking(textString,500)

        print(paragraphs)

        translated_chunks = []

        for chunk in paragraphs:
            # Translate each paragraph separately
            translated_chunk = translator_model.translate(chunk, languageInput, request.languageOutput)
            translated_chunks.append(translated_chunk)
        
        # 3. Join them back together
        resultTranslated = '\n\n'.join(translated_chunks)

        results.append({  "Original Text": textString,  "Original Language": languageInput, 
                        "Translated Text": resultTranslated, "Output language" : request.languageOutput })

    return results

@app.post("/simplifier")
def translator(request: SimplifierRequest):

    #retrieving list of text
    is_list = isinstance(request.text, list)
    texts_to_process = request.text if is_list else [request.text]

    if not texts_to_process or (not is_list and request.text == ""):
        texts_to_process = ["This is a sample text to help with some translations"]

    results = []

    for textString in texts_to_process:

        start = time.perf_counter()

        if request.languageInput == "":
            request.languageInput = translator_model.detect_language(textString)

        simplifierPrompt = GenerateSimplifierPrompt(textString, request.languageInput)

        resultSimplified = TriggerLLMOllama(simplifierPrompt)
        print("simplified text: " + resultSimplified)
        end = time.perf_counter()
        print(f"Total time: {end - start:.2f} s.")

        results.append({  "Original Text": textString,  "Language": request.languageInput, 
                        "simplified Text": resultSimplified })

    return results