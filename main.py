import pytesseract
import requests
from dotenv import load_dotenv
import os
from PIL import Image
from googletrans import Translator

load_dotenv()
tesseract_cmd = os.getenv("TESSERACT_CMD")
yandex_key =os.getenv("YANDEX_KEY")

pytesseract.pytesseract.tesseract_cmd = f"{tesseract_cmd}"

images=['test.png']

def start_translating(images):
    for image_path in images:
        image = Image.open(image_path)
        chinese_text = pytesseract.image_to_string(image, lang='chi_sim')
        chinese_text = chinese_text.replace('\n','')

        translate_with_google(chinese_text)
        # translate_with_yandex(chinese_text)

def translate_with_google(chinese_text):
    translator = Translator()
    translated_text = translator.translate(chinese_text, src='zh-cn', dest='en')
    print(f"translated from google {translated_text}")

def translate_with_yandex(chinese_text):
    endpoint = "https://translate.yandex.net/api/v1.5/tr.json/translate"
    params = {
        'key': yandex_key,
        'text': chinese_text,
        'lang': 'zh-en'
    }
    response = requests.post(endpoint, data=params)
    translated_text = response.json()['text'][0]
    print(f"translated from yandex {translated_text}")
    
start_translating(images)
