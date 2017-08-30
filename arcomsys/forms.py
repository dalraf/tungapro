from django import forms
from .models import Cliente
from django.forms import modelformset_factory

class clienteform(forms.ModelForm):
    nome = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Nome'})
        )

    class Meta:
        model = Cliente
        fields = ('nome', )


class filtrarcliente(forms.Form):
    filtro = forms.CharField(
    required=False,
    widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Filtrar'}
    ))


ListarClienteFormset = modelformset_factory(
    Cliente, 
    fields=('nome','registro'),
#    widgets={'nome': forms.TextInput(attrs={'readonly':'readonly','style': 'border: none'})},
    can_delete=True,
    extra=0
    )
