# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('produce', '0003_farm_agritype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farm',
            name='agritype',
            field=models.ForeignKey(related_query_name=b'farm', related_name='farms', on_delete=django.db.models.deletion.SET_NULL, to='produce.AgriType', null=True),
        ),
    ]
