# Generated by Django 2.1.7 on 2019-03-31 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topic', '0010_auto_20190331_0920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='zip_file',
            field=models.FileField(upload_to='docker/04f148cb-68af-41d0-ab37-4b9bdf314c3a', verbose_name='部署的压缩包'),
        ),
    ]