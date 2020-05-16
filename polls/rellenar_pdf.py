from io import BytesIO
from random import choice
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import mm
from PyPDF2 import PdfFileWriter, PdfFileReader
from datetime import datetime


class Crear_pdf():
    def __init__(self, pdf_file, elementos, save_file_dir):
        self.pdf_file = pdf_file
        self.elementos = elementos  # ((pagina, pos_x, pos_y, texto), ...)
        self.output = PdfFileWriter()
        self.write_pages(self.pdf_file, self.elementos)
        if save_file_dir[-1] != "/" or save_file_dir[-1] != "\\":
            save_file_dir += "/"
        self.create_pdf(save_file_dir)

    def write_pages(self, source_file, elements):
        read_pdf = PdfFileReader(open(source_file, "rb"))
        elements = list(elements)
        elements.sort()
        counter = 0
        for page in range(read_pdf.getNumPages()):
            packet = BytesIO()
            canv = canvas.Canvas(packet, pagesize=letter)
            for item_list in elements[counter:]:
                item_page = item_list[0]
                if item_page != page + 1:
                    break
                counter += 1
                pos_x = item_list[1]
                pos_y = item_list[2]
                text = item_list[3]
                canv.drawString(pos_x * mm, pos_y * mm, text)
            canv.save()
            new_page = PdfFileReader(packet)
            pdf_page = read_pdf.getPage(page)
            pdf_page.mergePage(new_page.getPage(0))
            self.output.addPage(pdf_page)

    def create_pdf(self, destino):
        self.file_save = destino + datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".pdf"
        outputStream = open(self.file_save, "wb")
        self.output.write(outputStream)
        outputStream.close()

    def create_file_name(self):
        file_name = ""
        for i in range(7):
            file_name += choice([chr(letter) for letter in range(ord("a"), ord("z") + 1)])
        return file_name
