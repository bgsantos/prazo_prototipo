import os
from pdfminer.pdfpage import PDFPage
from pdfminer.layout import LAParams
from pdfminer.converter import PDFPageAggregator
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter

# Uma alternativa é o Py2PDF, mas o encoding do módulo não funciona das melhores formas
# TODO : jogar toda essa rotina para a tools
dirname = os.path.split(__file__)[0]
file = open("{}/../static/20180808CAPDJETJRJ_1.pdf".format(dirname), 'rb')

laparams = LAParams()
pdfrm = PDFResourceManager()
parser = PDFParser(file)
document = PDFDocument(parser)
device = PDFPageAggregator(pdfrm, laparams=laparams)
interpreter = PDFPageInterpreter(pdfrm, device)
for page in PDFPage.create_pages(document):
    interpreter.process_page(page)
    layout = device.get_result()

for i in layout:
    print(i)
