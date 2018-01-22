# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Farm',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('estimated_size', models.IntegerField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('firstname', models.CharField(max_length=250)),
                ('lastname', models.CharField(max_length=250)),
                ('dob', models.DateField(null=True, blank=True)),
                ('gender', models.PositiveIntegerField()),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('added_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='farm',
            name='owner',
            field=models.ManyToManyField(related_query_name=b'farm', related_name='farms', to='produce.Person'),
        ),
    ]
