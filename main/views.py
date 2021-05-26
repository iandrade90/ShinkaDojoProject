from django.shortcuts import render
from .models import (
        Inicio,
        Acerca,
        Programa,
        Contacto,
        PresentacionEstilos,
        Estilo,
        Horario,
        Experto,
        Maestro
        )
from django.views import View
from django.core.mail import send_mail

class PageView(View):
    template_name = 'index.html'
    titulos = Inicio.objects.all()
    programas = Acerca.objects.all()
    clases = Programa.objects.all()
    slogans = Contacto.objects.all()
    presentaciones = PresentacionEstilos.objects.all()
    estilos = Estilo.objects.all()
    horarios = Horario.objects.all()
    expertos = Experto.objects.all()
    maestros = Maestro.objects.all()
    contexto = {
            'titulos': titulos, 
            'programas': programas,
            'clases': clases,
            'slogans': slogans,
            'presentaciones': presentaciones,
            'estilos': estilos,
            'horarios': horarios,
            'expertos': expertos,
            'maestros': maestros}

    def get(self, request):

        return render(request, self.template_name, self.contexto)

    def post(self, request):
        if request.method == 'POST':
            nombre = request.POST.get('name')
            email = request.POST.get('email')
            asunto = request.POST.get('subject')
            mensaje = request.POST.get('message')

            data = {
                    'nombre': nombre,
                    'email': email,
                    'asunto': asunto,
                    'mensaje': mensaje
                    }

            mensaje = '''
            Nombre: {}
            Mensaje: {}
            Email: {}
            '''.format(data['nombre'], data['mensaje'], data['email'])
            send_mail(data['asunto'], mensaje, '', ['contactoshinkadojo@gmail.com'])

        return render(request, self.template_name, self.contexto)
