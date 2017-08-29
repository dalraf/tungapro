# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from .models import *

from .forms import * 

# Create your views here.


def listarclientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'listarclientes.html', {'clientes': clientes})


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
