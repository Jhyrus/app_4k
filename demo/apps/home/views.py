# Create your views here.

from django.shortcuts import render_to_response
from django.template import RequestContext
from demo.apps.ventas.models import cliente
from demo.apps.home.forms import ContactForm
from django.core.mail import EmailMultiAlternatives # enviamos HTML

def index_view(request):
	return render_to_response('home/index.html',context_instance=RequestContext(request))

def about_view(request):
	mensaje = "Esto es un mensaje desde mi vista"
	ctx = {'msg':mensaje}
	return render_to_response('home/about.html',ctx,context_instance=RequestContext(request))

def clientes_view(request):
	prod = cliente.objects.filter(status=True) #Select * from ventas_productos where status = True
	ctx = {'clientes':prod}
	return render_to_response('home/clientes.html',ctx,context_instance=RequestContext(request))

def contacto_view (request):
	info_enviado = False #define si se envio o no
	email = ""
	titulo = ""
	texto = ""
	if request.method == "POST":
		formulario = ContactForm(request.POST)
		if formulario.is_valid():
			info_enviado = True
			email = formulario.cleaned_data['Email']
			titulo = formulario.cleaned_data['Titulo']
			texto = formulario.cleaned_data['Texto']

		# configuracion email

		to_admin = 'diego.morales.medrano@gmail.com'
		html_content = "informacion recibida de [%s] <br><br><br> ****Mensaje**<br><br>%s"%(email,texto)
		msg = EmailMultiAlternatives('Correo de Contacto',html_content,'from@server.com',[to_admin])
		msg.attach_alternative(html_content,'text/html') #definimos el contenido como HTML
		msg.send() #enviamos
	else:

		formulario = ContactForm()
	ctx = {'form':formulario,'email':email,'titulo':titulo,'texto':texto, 'info_enviado':info_enviado}
	return render_to_response('home/contacto.html',ctx,context_instance=RequestContext(request))
