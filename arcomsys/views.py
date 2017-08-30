# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from .models import *

from .forms import * 

# Create your views here.

def listarclientes(request):
    if request.method == 'POST':
        form = filtrarcliente(request.POST)
        if form.is_valid():
            filtro = form.cleaned_data['filtro']
            clientes = Cliente.objects.filter(nome__contains=filtro,)
            return render(request, 'listarclientes.html', {'clientes': clientes, 'form': form })
    else:
        clientes = Cliente.objects.all()
        formfilter = filtrarcliente()
        formset = ListarClienteFormset()
        return render(request, 'listarclientes.html', {'clientes': clientes, 'formfilter': formfilter, 'formset': formset })




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