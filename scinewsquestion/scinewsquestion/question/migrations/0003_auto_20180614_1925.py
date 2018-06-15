# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-06-14 19:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0002_annotquestion_question_pubdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='annotquestion',
            name='question_deletdate',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date deleted'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='annotquestion',
            name='question_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='genquestion',
            name='question_deleted',
            field=models.BooleanField(default=False),
        ),
    ]
