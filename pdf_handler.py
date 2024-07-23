from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph
import PyPDF2


def save_translated_text_to_pdf(translated_text, output_pdf_path):
    formatted_text = translated_text.replace("\n", "<br />")

    pdf = SimpleDocTemplate(output_pdf_path, pagesize=letter)
    styles = getSampleStyleSheet()
    text_paragraph = Paragraph(formatted_text, style=styles['Normal'])
    
    pdf.build([text_paragraph])

def read_from_pdf(file_path, total_page=None):
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        texts = []
        # Determine the range of pages to read
        num_pages = len(reader.pages)
        pages_to_read = total_page if total_page is not None else num_pages
        
        # Ensure we don't exceed the number of available pages
        pages_to_read = min(pages_to_read, num_pages)

        for i in range(pages_to_read):
            text = reader.pages[i].extract_text() or ""
            texts.append(text)

    return texts
