# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-18 17:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0012_auto_20170616_1806'),
    ]

    operations = [
        migrations.CreateModel(
            name='PurchaseItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('free', models.IntegerField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.Item')),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseMemo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('discount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('paid', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
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
            model_name='purchasememo',
            name='party',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.Customer'),
        ),
        migrations.AddField(
            model_name='purchasememo',
            name='purchase_item',
            field=models.ManyToManyField(to='project.PurchaseItem'),
        ),
    ]