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
            filtro = formfilter.cleaned_data['filtro']
            formset = ListarClienteFormset(queryset=Cliente.objects.filter(nome__contains=filtro),)
            return render(request, 'listarclientes.html', {'formfilter': formfilter, 'formset': formset })
        elif formfilter.is_valid() and 'Deletar' in request.POST:
            formset = ListarClienteFormset(request.POST)
            if formset.is_valid():
                formset.save()
            filtro = formfilter.cleaned_data['filtro']
            formset = ListarClienteFormset(queryset=Cliente.objects.filter(nome__contains=filtro),)
            return render(request, 'listarclientes.html', {'formfilter': formfilter, 'formset': formset })
        else:
            formfilter = filtrarcliente()
            formset = ListarClienteFormset()
            return render(request, 'listarclientes.html', {'formfilter': formfilter, 'formset': formset })
            
    else:
        formfilter = filtrarcliente()
        formset = ListarClienteFormset()
        return render(request, 'listarclientes.html', {'formfilter': formfilter, 'formset': formset })




def addclientes(request):
    if request.method == 'POST':
        form = clienteform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listarclientes')
    else:
        form = clienteform()
    return render(request, 'addcliente.html', {
        'form': form
    })

def deletarcliente(request, pk):
    clientquery = Cliente.objects.filter(pk=pk,)
    clientquery.delete()
    return redirect('listarclientes')