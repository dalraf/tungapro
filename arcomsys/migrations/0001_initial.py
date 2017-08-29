# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-29 14:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=150, null=True, verbose_name='Nome')),
            ],
        ),
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=150, null=True, verbose_name='Nome')),
                ('telefone', models.CharField(blank=True, max_length=12, null=True, verbose_name='Telefone')),
                ('email', models.CharField(blank=True, max_length=12, null=True, verbose_name='Email')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='arcomsys.Cliente')),
            ],
        ),
    ]
