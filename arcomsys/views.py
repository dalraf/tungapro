# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import Cliente

# Create your views here.

def listarclientes(request):
    clientes = Cliente.objects.all()
    return render(request,'listarclientes.html', {'clientes': clientes})
