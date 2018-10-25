from django.shortcuts import render
from django.views import generic
from .models import Despacho
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus.tables import Table
cm = 2.54

from reportlab.lib.units import inch
from reportlab.lib.pagesizes import A4
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER, TA_LEFT, TA_RIGHT
import json
import time
import datetime

# Create your views here.

class DespachosListView(generic.ListView):
    model = Despacho
    template_name = 'base.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ndespachos'] = Despacho.objects.filter(status=1).count()
        return context

PAGE_WIDTH = A4[0]
PAGE_HEIGHT = A4[1]

def header(canvas, doc):
    canvas.saveState()
    canvas.drawImage("static/img/bolivar.jpg", 60, 750, 90, 80,preserveAspectRatio=True)
    canvas.drawImage("static/img/corporacion.png", 60, 30, 90, 80,preserveAspectRatio=True)
    canvas.drawImage("static/img/iso.png", 450, 30, 90, 80,preserveAspectRatio=True)
    canvas.drawImage("static/img/transbolivar.png", 430, 750, 90, 80,preserveAspectRatio=True)
    canvas.restoreState()


def write_pdf_view(request):
    fecha = "" 
    status = ""
    
    if(request.POST.get("fecha") != None):
        fecha = request.POST.get("fecha")
    if(request.POST.get("status") != None):
        status = request.POST.get("status")
    doc = SimpleDocTemplate("/tmp/somefilename.pdf")
    Story = []
 
    ps = ParagraphStyle('parrafos',
                           alignment = TA_CENTER,
                           fontSize = 12,
                           fontName="Times-Roman")

    text = "<table> <thead><tr><th>CODIGO</th><th>HORA</th><th>UNIDAD</th></tr></thead><tbody><tr><td>321</td><td>123</td></tr></tbody></table>"
    p = Paragraph(text, ps)
    Story.append(p)
    Story.append(Spacer(1,0.4*inch))
    doc.build(Story, header)

    fs = FileSystemStorage("/tmp")
    with fs.open("somefilename.pdf") as pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'filename="somefilename.pdf"'
        return response

    return response





    