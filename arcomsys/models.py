# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Cliente(models.Model):
    nome = models.CharField("Nome",max_length=50, blank=True, null=True)
    marcar_delecao = models.BooleanField(default=False)
    
    def __unicode__(self):
        return self.nome

class Contato(models.Model):
    nome = models.CharField("Nome",max_length=50, blank=True, null=True)
    telefone = models.CharField("Telefone",max_length=12, blank=True, null=True)
    email = models.CharField("Email",max_length=12, blank=True, null=True)
    client = models.ForeignKey('Cliente', on_delete=models.CASCADE )

    def __unicode__(self):
        return self.nome