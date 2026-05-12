import requests
from ollama import Client
#libs for measuring performance
import time
import psutil
import os

configuration = "cloud"

def TriggerLLMOllama (prompt: str = ""):

    LLMresult = ""

    if prompt != "":
        if configuration == "local":
            #This runs the ollama model in a local manner
            start = time.perf_counter()
            url = "http://localhost:11434/api/chat"
            jsonRequest = {
                "model": "llama3:latest",
                "messages": [
                    { 
                    "role": "user", 
                    "content": prompt
                    }
                ],
                "stream": False
            }

            LLMresponse = requests.post(
                url,
                json = jsonRequest
            )

            end = time.perf_counter()

            print("The LLM responded with the following status: " + str(LLMresponse.status_code) )

            process = psutil.Process(os.getpid())
            cpu = process.cpu_percent(interval=None) 
            ram_mb = process.memory_info().rss / (1024 ** 2)

            print(f"--- LLM Stats ---")
            print(f"RAM: {ram_mb:.2f} MB | Time: {end - start:.4f}s")

            LLMresult = LLMresponse.json()["message"]["content"]
        else:
            #this runs the model on the cloud
            client = Client(
                host="https://api.ollama.com",
                headers={
                    "Authorization": f"Bearer {OLLAMA_API_KEY}"
                }
            )

            messages = [
            {
                'role': 'user',
                'content': prompt,
            },
            ]

            for part in client.chat('gpt-oss:120b-cloud', messages=messages, stream=True):
                LLMresult = LLMresult + part['message']['content']
    else:
        print("You need to generate a prompt to run the LLM")


    return LLMresult