from django.shortcuts import render
from .models import (
        Inicio,
        Acerca,
        Programa,
        Contacto,
        PresentacionEstilos,
        Estilo
        )
from django.views.generic import ListView

class InicioLista(ListView):
  template_name = 'index.html'
  context_object_name = 'titulos'
  queryset = Inicio.objects.all()

  def get_context_data(self, **kwargs):
    context = super(InicioLista, self).get_context_data(**kwargs)
    context['programas'] = Acerca.objects.all()
    context['clases'] = Programa.objects.all()
    context['slogans'] = Contacto.objects.all()
    context['presentaciones'] = PresentacionEstilos.objects.all()
    context['estilos'] = Estilo.objects.all()
    return context
