from django.db import models

class Inicio(models.Model):
  titulo_barra_uno = models.CharField(max_length=30)
  titulo_barra_dos = models.CharField(max_length=30)
  subtitulo = models.CharField(max_length=30)
  titulo_uno = models.CharField(max_length=30)
  titulo_dos = models.CharField(max_length=30)

  def __str__(self):
    return 'Titulos de la pagina inicio'

class Acerca(models.Model):
  titulo_programa_uno = models.CharField(max_length=30, null=False)
  titulo_programa_dos = models.CharField(max_length=30)
  contenido = models.CharField(max_length=200)
  inicio = models.ForeignKey(Inicio, related_name='acerca', on_delete=models.SET_NULL, null=True)