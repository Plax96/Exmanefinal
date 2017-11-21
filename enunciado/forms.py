from django import forms
from .models import *
from django.contrib.auth.models import User

class GradoForm(forms.ModelForm):
    class Meta:
        model = Grado
        fields = ('nombre','seccion')
        #widget = forms.TextInput(
        #attrs = {'class': 'summernote', 'name': 'subject'}
        #)

class Gestion_gradoForm(forms.ModelForm):
    class Meta:
        model = Gestion_grado
        fields = ('grado','materia')
