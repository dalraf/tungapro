from django import forms
from .models import Cliente

class clienteform(forms.ModelForm):
    nome = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Nome'}))

    class Meta:
        model = Cliente
        fields = ('nome', )