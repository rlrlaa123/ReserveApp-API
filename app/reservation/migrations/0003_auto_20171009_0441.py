# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-08 19:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0002_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'managed': False, 'verbose_name': '\ubb38\uc758\uc0ac\ud56d \ub313\uae00 \uad00\ub9ac', 'verbose_name_plural': '\ubb38\uc758 \uc0ac\ud56d \ub313\uae00'},
        ),
        migrations.AlterModelOptions(
            name='inquire',
            options={'managed': False, 'verbose_name': '\ubb38\uc758\uc0ac\ud56d', 'verbose_name_plural': '\ubb38\uc758\uc0ac\ud56d'},
        ),
        migrations.AlterModelOptions(
            name='notice',
            options={'managed': False, 'verbose_name': '\uacf5\uc9c0', 'verbose_name_plural': '\uacf5\uc9c0'},
        ),
        migrations.AlterModelOptions(
            name='reservation',
            options={'managed': False, 'verbose_name': '\uac15\uc758\uc2e4 \ub300\uc5ec', 'verbose_name_plural': '\uac15\uc758\uc2e4 \ub300\uc5ec'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'managed': False, 'verbose_name': '\uc720\uc800 \uad00\ub9ac', 'verbose_name_plural': '\uc720\uc800 \uad00\ub9ac'},
        ),
    ]