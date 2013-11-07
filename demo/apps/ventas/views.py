# Create your views here.

from django.shortcuts import render_to_response
from django.template import RequestContext
from demo.apps.ventas.forms import addClientForm
from demo.apps.ventas.models import cliente


def add_cliente_view(request):
	if request.method == "POST":
	 	form = addClientForm(request.POST)
		info = "Inicializando"
		if form.is_valid():
			nombre = form.cleaned_data['nombre']
			apellido = form.cleaned_data['apellido']
			ci = form.cleaned_data['ci']
			telefono = form.cleaned_data['telefono']
			p = cliente()
			p.nombre = nombre
			p.apellido = apellido
			p.ci = ci
			p.telefono = telefono
			p.status = True
			p.save() #Guardar info
			info = "Se guardo satisfactoriamente!!!"
		else:
			info = "datos incorrectos"
		form = addClientForm()
		ctx = {'form':form,'informacion':info}
		return render_to_response ('ventas/addCliente.html',ctx,context_instance=RequestContext(request))
	else: #GET
		form = addClientForm()
		ctx = {'form':form}
		return render_to_response('ventas/addCliente.html',ctx,context_instance=RequestContext(request))
