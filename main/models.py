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

  def __str__(self):
      return 'Titulo de la sesion de programas'


class Programa(models.Model):
    titulo = models.CharField(max_length=100)
    contenido = models.CharField(max_length=100)

    def __str__(self):
        return 'Programa ' + self.titulo

class Contacto(models.Model):
    titulo_uno = models.CharField(max_length=30)
    enfasis_uno = models.CharField(max_length=30)
    titulo_dos = models.CharField(max_length=30)
    enfasis_dos = models.CharField(max_length=30)
    contenido = models.CharField(max_length=200)

    def __str__(self):
        return 'Slogan de contacto'


class PresentacionEstilos(models.Model):
    titulo = models.CharField(max_length=30)
    enfasis = models.CharField(max_length=30)
    contenido = models.CharField(max_length=200)

    def __str__(self):
        return 'Nuestros Estilos'

class Estilo(models.Model):
    titulo = models.CharField(max_length=30)
    resumen = models.CharField(max_length=200)
    contenido = models.CharField(max_length=2000)

    def __str__(self):
        return 'Estilo ' + self.titulo


class Horario(models.Model):
    titulo = models.CharField(max_length=30)
    enfasis = models.CharField(max_length=30)
    contenido = models.CharField(max_length=100)

    def __str__(self):
        return 'Horario de clases'

class Experto(models.Model):
    titulo = models.CharField(max_length=30)
    enfasis = models.CharField(max_length=30)
    contenido = models.CharField(max_length=200)

    def __str__(self):
        return 'Titulo de Expertos'

class Maestro(models.Model):
    disciplina = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    imagen = models.ImageField(null=True, upload_to='images')
    contenido = models.CharField(max_length=250)
    instagram = models.CharField(max_length=100, blank=True)
    facebook = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.nombre
