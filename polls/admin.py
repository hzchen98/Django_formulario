# -*- coding: utf-8 -*-
from itertools import chain

from django.contrib import admin
from .models import GenPdf, PdfPosition


# Register your models here.

class PositionInline(admin.TabularInline):
    model = PdfPosition
    extra = 3

# Personalización de la vista a mostrar en admin del modelo PdfPosition
class PdfAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['pdf_name']}),
        ('Archivo PDF', {'fields': ['origin_pdf', 'published']})
    ]
    inlines = [PositionInline]
    list_display = ['pdf_name']
    search_fields = ['pdf_name']
    list_filter = ['pdf_name']


admin.sites.AdminSite.site_header = "Administración de formularios"
admin.site.register(GenPdf, PdfAdmin)
