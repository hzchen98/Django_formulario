
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views import generic
from .models import GenPdf
from .rellenar_pdf import Crear_pdf

# Create your views here.


class IndexView(generic.ListView):
    template_name = 'formulario/pdfs.html'
    context_object_name = 'latest_pdf_list'

    def get_queryset(self):
        return GenPdf.objects.filter(published=True).order_by('pdf_name')


class DetailView(generic.DetailView):
    model = GenPdf
    template_name = "formulario/detail.html"

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if not self.object.published:
            return HttpResponseRedirect("/")
        else:
            context = self.get_context_data(object=self.object)
            return self.render_to_response(context)

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
    file_save_dir = "polls/download_files/" + pdf.pdf_name.replace(" ", "_")
    write_pdf = Crear_pdf(origin_file, position_list, file_save_dir)
    with open(write_pdf.file_save, 'rb') as client_pdf:
        response = HttpResponse(client_pdf.read(), content_type='text/download')
        response['Content-Disposition'] = 'attachment;filename=' + pdf.pdf_name.replace(" ", "_") + "_" + write_pdf.generated_name
        response.set_cookie("descarga", "true")
        return response
