from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from .models import GenPdf
from django.utils import timezone
from io import BytesIO
from random import choice
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from PyPDF2 import PdfFileWriter, PdfFileReader
from .rellenar_pdf import Crear_pdf
from django.conf import settings

# Create your views here.


class IndexView(generic.ListView):
	template_name = 'formulario/pdfs.html'
	context_object_name = 'latest_pdf_list'
	def get_queryset(self):
		return GenPdf.objects.all().order_by('pdf_name')
	
class DetailView(generic.DetailView):
	model = GenPdf
	template_name = "formulario/detail.html"

	def get_queryset(self):
		return GenPdf.objects.all()

def create_pdf(request, genpdf_id):
	pdf = get_object_or_404(GenPdf, pk=genpdf_id)
	position_list = list()
	for item in pdf.pdfposition_set.all():
		page = item.pdf_page
		pos_x = float(item.position_x)
		pos_y = float(item.position_y)
		text = request.POST[str(item)]
		position_list.append((page, pos_x, pos_y, text))
	origin_file = str(pdf.origin_pdf)
	file_save_dir = "polls/download_files"
	write_pdf = Crear_pdf(origin_file, position_list, file_save_dir)
	with open(write_pdf.file_save, 'rb') as client_pdf:
		response = HttpResponse(client_pdf.read(), content_type='text/download')
		response['Content-Disposition'] = 'inline;filename=formulario.pdf'
		return response