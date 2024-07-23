import pytesseract
from dotenv import load_dotenv
import os
from PIL import Image
from googletrans import Translator
from pdf_handler import save_translated_text_to_pdf
import re
from xml.sax.saxutils import escape


load_dotenv()
tesseract_cmd = os.getenv("TESSERACT_CMD")
yandex_key =os.getenv("YANDEX_KEY")


pytesseract.pytesseract.tesseract_cmd = f"{tesseract_cmd}"



def start_translating(images, saved_file_name):
    translated_texts=""
    for image_path in images:
        image = Image.open(image_path)
    
        chinese_text = pytesseract.image_to_string(image, lang='chi_sim')
        if len(chinese_text)< 10:
            print(image_path)
            
        translated_text = translate_with_google(chinese_text.replace('\n',' '))
        formatted_text = remove_html_tags(translated_text) 
        
        translated_texts += formatted_text
        
    save_translated_text_to_pdf(translated_texts,saved_file_name)

def translate_with_google(chinese_text):
    translator = Translator()
    try:
        response = translator.translate(chinese_text, src='zh-cn', dest='en')
        
        if response and hasattr(response, 'text'):
            translated_texts = response.text
            return translated_texts
        else:
            print("Unexpected response structure or empty response from API.")
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
  
def remove_html_tags(text):
    clean_text = re.sub(r'<.*?>', '', text)
    clean_text = escape(clean_text, entities={"&": "&amp;", "<": "&lt;", ">": "&gt;"})
    return clean_text


def get_image_file_paths(root_folder):
    # List to hold all the image file paths
    image_file_paths = []
    
    # Walk through the directory
    for dirpath, dirnames, filenames in os.walk(root_folder):
        for filename in filenames:
            if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
                image_file_paths.append(os.path.join(dirpath, filename))
    
    return image_file_paths

root_folder = 'image/lastChap'
saved_file_name = 'pdf/translated/lastChap.pdf'

# Get all image file paths
image_paths = get_image_file_paths(root_folder)

start_translating(image_paths, saved_file_name)
