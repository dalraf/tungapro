from django import forms
from .models import Cliente

class clienteform(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('nome', )