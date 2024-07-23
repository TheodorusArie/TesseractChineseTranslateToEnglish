from dotenv import load_dotenv
import os
import requests
import json
from pdf_handler import read_from_pdf, save_translated_text_to_pdf

load_dotenv()
open_ai_key = os.getenv("OPEN_AI_KEY")


def paraphrase_with_openai(text):
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {open_ai_key}",
        "OpenAi-Project":"proj_o2HSPC5IEcfJCHEqWCfEZkpv"
    }

    payload = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "user", "content": f"Please restructure the following sentences to improve coherence and readability:\n\n{text}"}
            ],
        "temperature": 0.7
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload))

    # Print the response
    if response.status_code == 200:
        response_data = response.json()
        return response_data['choices'][0]['message']['content'].strip()
        
    else:
        print(f"Request failed with status code {response.status_code}: {response.text}")

texts= read_from_pdf("pdf/translated/lastChap.pdf")
open_ai_text = ""
for page_text in texts:
    # print(page_text)
    restructured_text = paraphrase_with_openai(page_text)
    open_ai_text += restructured_text + '\n'
save_translated_text_to_pdf(open_ai_text, "pdf/paraphrase/lastChap.pdf")