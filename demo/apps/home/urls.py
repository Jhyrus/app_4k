from django.conf.urls.defaults import patterns,url

urlpatterns = patterns('demo.apps.home.views',
	url(r'^$','index_view',name='vista_principal'),
	url(r'^about/$','about_view', name='vista_about'),
	url(r'^clientes/$','clientes_view', name='vista_clientes'),
	url(r'^contacto/$','contacto_view',name='vista_contacto'),
)

