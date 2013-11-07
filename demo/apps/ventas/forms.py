from django import forms

class addClientForm (forms.Form):
	nombre = forms.CharField(widget=forms.TextInput())
	apellido = forms.CharField(widget=forms.TextInput())
	ci = forms.CharField(widget=forms.TextInput())
	telefono = forms.CharField(widget=forms.TextInput())

	def clean(self):
		return self.cleaned_data
