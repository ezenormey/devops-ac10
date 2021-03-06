# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=200)),
                ('periodo', models.CharField(max_length=50)),
                ('instituicao', models.CharField(max_length=200)),
            ],
        ),
    ]
    
    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidatos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=200)),
                ('vestibular', models.CharField(max_length=50)),
            ],
        ),
    ]
