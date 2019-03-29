# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-03-29 08:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topic', '0009_auto_20190328_2246'),
    ]

    operations = [
        migrations.RenameField(
            model_name='topicinstance',
            old_name='team_id',
            new_name='team',
        ),
        migrations.RenameField(
            model_name='topicinstance',
            old_name='topic_id',
            new_name='topic',
        ),
        migrations.AddField(
            model_name='topicinstance',
            name='container_id',
            field=models.CharField(max_length=16, null=True, verbose_name='容器ID'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='zip_file',
            field=models.FileField(upload_to='docker/212c0aae-51f9-11e9-962e-b025aa148d03', verbose_name='部署的压缩包'),
        ),
    ]
