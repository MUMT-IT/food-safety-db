# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('produce', '0002_auto_20180122_0843'),
    ]

    operations = [
        migrations.AddField(
            model_name='farm',
            name='agritype',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, to='produce.AgriType', null=True),
        ),
    ]
