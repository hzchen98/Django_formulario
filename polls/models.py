import datetime
from django.db import models
from django.utils import timezone


# Create your models here.
class GenPdf(models.Model):
    pdf_name = models.CharField(max_length=200)
    origin_pdf = models.FileField(upload_to="polls/upload")

    def __str__(self):
        return self.pdf_name

class PdfPosition(models.Model):
    pdf = models.ForeignKey(GenPdf, on_delete=models.CASCADE)
    position_text = models.CharField(max_length=100)
    position_x = models.DecimalField(decimal_places=2,max_digits=200)
    position_y = models.DecimalField(decimal_places=2,max_digits=299)
    pdf_page = models.IntegerField(default=1)

    def __str__(self):
        return self.position_text