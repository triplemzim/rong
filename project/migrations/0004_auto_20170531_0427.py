# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-30 22:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_customer_supplier'),
    ]

    operations = [
        migrations.CreateModel(
            name='SandC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=150)),
                ('mobile_no', models.CharField(max_length=20)),
                ('type', models.CharField(max_length=20)),
                ('sr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.Sr')),
            ],
        ),
        migrations.RemoveField(
            model_name='customer',
            name='sr',
        ),
        migrations.RemoveField(
            model_name='supplier',
            name='sr',
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
        migrations.DeleteModel(
            name='Supplier',
        ),
    ]
