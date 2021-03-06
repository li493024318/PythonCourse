# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-06-27 07:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('t7', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='班级名字')),
                ('type', models.CharField(max_length=20, verbose_name='班级类型')),
            ],
        ),
        migrations.CreateModel(
            name='MyBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='书名')),
                ('content', tinymce.models.HTMLField()),
            ],
        ),
        migrations.AddField(
            model_name='stu',
            name='grade',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='t7.Grade', verbose_name='所属班级'),
        ),
    ]
