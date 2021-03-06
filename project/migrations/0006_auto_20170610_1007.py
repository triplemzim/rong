# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-10 04:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0005_auto_20170531_0432'),
    ]

    operations = [
        migrations.CreateModel(
            name='Memo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='SaleItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.Item')),
            ],
        ),
        migrations.AlterField(
            model_name='customer',
            name='sr',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.Sr'),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='sr',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.Sr'),
        ),
        migrations.AddField(
            model_name='memo',
            name='item',
            field=models.ManyToManyField(to='project.SaleItem'),
        ),
        migrations.AddField(
            model_name='memo',
            name='party',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.Customer'),
        ),
        migrations.AddField(
            model_name='memo',
            name='sr',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.Sr'),
        ),
    ]
