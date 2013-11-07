from django.conf.urls.defaults import patterns,url
urlpatterns = patterns('demo.apps.ventas.views',
	url(r'^add/cliente/$','add_cliente_view',name="vista_agregar_cliente"),
)
