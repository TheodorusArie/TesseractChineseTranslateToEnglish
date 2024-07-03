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

image_path = 'test.png'

image = Image.open(image_path)

chinese_text = pytesseract.image_to_string(image, lang='chi_sim')
chinese_text = chinese_text.replace('\n','')

# free translator
translator = Translator()
google_translated_text = translator.translate(chinese_text, src='zh-cn', dest='en')

# paid translator
endpoint = "https://translate.yandex.net/api/v1.5/tr.json/translate"
params = {
    'key': yandex_key,
    'text': chinese_text,
    'lang': 'zh-en'
}

response = requests.post(endpoint, data=params)
translated_text = response.json()['text'][0]

# Print the extracted text
print(chinese_text)
print(translated_text)
print(google_translated_text)
