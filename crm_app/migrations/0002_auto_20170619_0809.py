# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-19 02:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='account_company_name',
            field=models.ForeignKey(db_column='account_companyname', on_delete=django.db.models.deletion.CASCADE, to='crm_app.Account'),
        ),
    ]
