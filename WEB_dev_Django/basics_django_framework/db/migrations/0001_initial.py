# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-03-26 15:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='topic',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.User'),
        ),
        migrations.AddField(
            model_name='topic',
            name='blog',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.Blog'),
        ),
        migrations.AddField(
            model_name='topic',
            name='likes',
            field=models.ManyToManyField(related_name='likes', to='db.User'),
        ),
        migrations.AddField(
            model_name='blog',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.User'),
        ),
        migrations.AddField(
            model_name='blog',
            name='subscribers',
            field=models.ManyToManyField(related_name='subscriptions', to='db.User'),
        ),
    ]
