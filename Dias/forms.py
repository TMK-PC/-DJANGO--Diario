from django import forms 
from .models import Dias

class DiaForm(forms.ModelForm):
    class Meta:
        model= Dias
        fields = ['data', 'topicos', 'descricao']