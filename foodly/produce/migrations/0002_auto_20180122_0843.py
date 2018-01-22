# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produce', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AgriType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('agtype', models.CharField(max_length=250)),
            ],
        ),
        migrations.RenameField(
            model_name='farm',
            old_name='owner',
            new_name='owners',
        ),
        migrations.AddField(
            model_name='farm',
            name='duration',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='farm',
            name='estimated_leased_size',
            field=models.DecimalField(null=True, max_digits=5, decimal_places=2, blank=True),
        ),
        migrations.AddField(
            model_name='farm',
            name='estimated_owned_size',
            field=models.DecimalField(null=True, max_digits=5, decimal_places=2, blank=True),
        ),
        migrations.AddField(
            model_name='person',
            name='relatives',
            field=models.ManyToManyField(related_name='_person_relatives_+', to='produce.Person'),
        ),
        migrations.AlterField(
            model_name='farm',
            name='estimated_size',
            field=models.DecimalField(null=True, max_digits=5, decimal_places=2, blank=True),
        ),
    ]
