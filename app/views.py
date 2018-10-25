from django.shortcuts import render
from django.views import generic
from .models import Despacho
import datetime

# Create your views here.

class DespachosListView(generic.ListView):
    model = Despacho
    template_name = 'base.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ndespachos'] = Despacho.objects.filter(status=1).count()
        return context


def reporte(request):
    return "hola"