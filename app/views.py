from django.shortcuts import render
from django.views import generic
from .models import Activa, Ruta, Operador
import datetime

# Create your views here.

class ActivasListView(generic.View):
    template_name = 'base.html'

    def get(self, request, *args, **kwargs):
        a = Activa.objects.all()
        context = {
            'activa': a
        }

        return render(request, self.template_name, context)