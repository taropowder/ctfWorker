# Generated by Django 2.1.7 on 2019-03-31 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topic', '0011_auto_20190331_0921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='zip_file',
            field=models.FileField(upload_to='docker/644755fd-869c-4684-b671-7f00ee0306d5', verbose_name='部署的压缩包'),
        ),
    ]
