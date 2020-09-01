from io import StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from searchPDF import settings
import os

filesText = {}

def extractText():
    for filename in os.listdir(settings.STATIC_ROOT + '/Data'):
        with open(os.path.join(settings.STATIC_ROOT + '/Data', filename), 'rb') as file:
            extracted_text = convert(file)
            filesText[filename] = extracted_text

def convert(infile, pages=None):
    if not pages:
        pagenums = set()
    else:
        pagenums = set(pages)

    output = StringIO()
    manager = PDFResourceManager()
    converter = TextConverter(manager, output, laparams=LAParams())
    interpreter = PDFPageInterpreter(manager, converter)

    for page in PDFPage.get_pages(infile, pagenums):
        interpreter.process_page(page)
    converter.close()
    text = output.getvalue()
    output.close
    return text