from django.db import models

# Create your models here.

class cliente(models.Model):
	nombre		= models.CharField(max_length=200)
	apellido	= models.CharField(max_length=200)
	ci			= models.CharField(max_length=200)
	telefono	= models.CharField(max_length=200)
	status		= models. BooleanField(default=True)

	def __unicode__(self):
		nombreCompleto = "%s %s"%(self.nombre,self.apellido)
		return nombreCompleto
