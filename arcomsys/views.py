# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from .models import *

from .forms import * 

# Create your views here.

def listarclientes(request):
    if request.method == 'POST':
        formfilter = filtrarcliente(request.POST)
        if formfilter.is_valid() and 'Filtrar' in request.POST:
            formadd = addclienteform()
            filtro = formfilter.cleaned_data['filtro']
            formset = ListarClienteFormset(queryset=Cliente.objects.filter(nome__contains=filtro),)
            return render(request, 'listarclientes.html', {'formfilter': formfilter, 'formset': formset })
        elif formfilter.is_valid() and 'Deletar' in request.POST:
            formset = ListarClienteFormset(request.POST)
            if formset.is_valid():
                formset.save()
            formadd = addclienteform()
            filtro = formfilter.cleaned_data['filtro']
            formset = ListarClienteFormset(queryset=Cliente.objects.filter(nome__contains=filtro),)
            return render(request, 'listarclientes.html', {'formadd': formadd,'formfilter': formfilter, 'formset': formset })
        elif formfilter.is_valid() and 'Adicionar' in request.POST:
            formadd = addclienteform(request.POST)
            if formadd.is_valid():
                formadd.save()
            filtro = formfilter.cleaned_data['filtro']
            formset = ListarClienteFormset(queryset=Cliente.objects.filter(nome__contains=filtro),)
            return render(request, 'listarclientes.html', {'formadd': formadd,'formfilter': formfilter, 'formset': formset })
        else:
            formadd = addclienteform()
            formfilter = filtrarcliente()
            formset = ListarClienteFormset()
            return render(request, 'listarclientes.html', {'formadd': formadd,'formfilter': formfilter, 'formset': formset })
            
    else:
        formadd = addclienteform()
        formfilter = filtrarcliente()
        formset = ListarClienteFormset()
        return render(request, 'listarclientes.html', {'formadd': formadd, 'formfilter': formfilter, 'formset': formset })

