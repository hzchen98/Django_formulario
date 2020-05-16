from PyPDF2 import PdfFileReader
from django.core.exceptions import ValidationError
from django.db import models
import os


# Create your models here.
class GenPdf(models.Model):
    pdf_name = models.CharField(max_length=200)
    origin_pdf = models.FileField(upload_to="polls/upload",
                                  null=True,
                                  verbose_name='file ')
    published = models.BooleanField(default=True, help_text="Publicado")

    def __str__(self):
        return self.pdf_name

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        super(GenPdf, self).save(force_insert, force_update, using, update_fields)
        directorio = self.pdf_name.replace(".pdf", "")
        directorio = directorio.replace(" ", "_")
        if not os.path.exists("polls/download_files/" + directorio):
            os.mkdir("polls/download_files/" + directorio)


class PdfPosition(models.Model):
    pdf = models.ForeignKey(GenPdf, on_delete=models.CASCADE)
    position_text = models.CharField(max_length=100)
    position_x = models.DecimalField(decimal_places=2, max_digits=299, default=0,
                                     help_text="Milímetros contando desde la esquina inferior izquierdo de la hoja")
    position_y = models.DecimalField(decimal_places=2, max_digits=399, default=0,
                                     help_text="Milímetros contando desde la esquina inferior izquierdo de la hoja")
    pdf_page = models.IntegerField(default=1)
    required = models.BooleanField(default=True, help_text="Obligatorios a rellenar")

    def __str__(self):
        return self.position_text

    def clean(self):
        read_pdf = PdfFileReader(self.pdf.origin_pdf.open("rb"))
        if self.pdf_page < 1 or self.pdf_page > read_pdf.getNumPages():
            raise ValidationError("Número de página incorrecto!")
        if self.position_x < 0 or self.position_y < 0:
            raise ValidationError("Las posiciones no pueden ser negativos!")
