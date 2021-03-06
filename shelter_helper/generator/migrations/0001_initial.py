# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-08 10:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ARC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arc_type_of_job', models.CharField(max_length=200)),
                ('arc_name', models.CharField(max_length=200)),
                ('arc_union_no', models.CharField(max_length=200)),
                ('arc_authority', models.CharField(max_length=200)),
                ('arc_data_of_issue', models.CharField(max_length=200)),
                ('arc_purpose_of_residence', models.CharField(max_length=200)),
                ('arc_residence_address', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Passport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('passport_no', models.CharField(max_length=30)),
                ('passport_nation', models.CharField(max_length=100)),
                ('passport_first_name', models.CharField(max_length=100)),
                ('passport_middle_name', models.CharField(max_length=100)),
                ('passport_last_name', models.CharField(max_length=100)),
                ('passport_issue_date', models.CharField(max_length=100)),
                ('passport_expire_date', models.CharField(max_length=100)),
                ('passport_birth', models.CharField(max_length=100)),
                ('passport_sex', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='arc',
            name='arc_passport_info',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='generator.Passport'),
        ),
    ]
