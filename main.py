import pytesseract
import requests
from dotenv import load_dotenv
import os
from PIL import Image
from googletrans import Translator
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.units import inch


load_dotenv()
tesseract_cmd = os.getenv("TESSERACT_CMD")
yandex_key =os.getenv("YANDEX_KEY")


pytesseract.pytesseract.tesseract_cmd = f"{tesseract_cmd}"

images=['test.png']

def start_translating(images):
    translated_texts=""
    for image_path in images:
        image = Image.open(image_path)
        chinese_text = pytesseract.image_to_string(image, lang='chi_sim')
        translated_text = translate_with_google(chinese_text.replace('\n',' ')) 
        print(translated_text)

    save_translated_text_to_pdf(translated_texts,"test_text.pdf")

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
  
def save_translated_text_to_pdf( translated_text, output_pdf_path):
    pdf = SimpleDocTemplate(output_pdf_path, pagesize=letter)
    styles = getSampleStyleSheet()
    text_paragraph = Paragraph(translated_text, style=styles['Normal'])
    pdf.build([text_paragraph])


def get_image_file_paths(root_folder):
    # List to hold all the image file paths
    image_file_paths = []
    
    # Walk through the directory
    for dirpath, dirnames, filenames in os.walk(root_folder):
        for filename in filenames:
            if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
                image_file_paths.append(os.path.join(dirpath, filename))
    
    return image_file_paths

root_folder = 'image'

# Get all image file paths
image_paths = get_image_file_paths(root_folder)

start_translating(image_paths)
