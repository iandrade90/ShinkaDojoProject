from django.shortcuts import render
from .models import Inicio, Acerca
from django.views.generic import ListView

class InicioLista(ListView):
  template_name = 'index.html'
  context_object_name = 'titulos'
  queryset = Inicio.objects.all()

  def get_context_data(self, **kwargs):
    context = super(InicioLista, self).get_context_data(**kwargs)
    context['programas'] = Acerca.objects.all()
    return context