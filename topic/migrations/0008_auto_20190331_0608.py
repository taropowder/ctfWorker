# Generated by Django 2.1.7 on 2019-03-31 06:08

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('topic', '0007_auto_20190331_0319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='uuid',
            field=models.CharField(default=uuid.UUID('da54068f-a05e-4398-96ef-1edfe2dc5de1'), max_length=8, unique=True, verbose_name='队伍ID'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='zip_file',
            field=models.FileField(upload_to='docker/6bcc863a-67bd-4cae-915c-36a06a33e0ad', verbose_name='部署的压缩包'),
        ),
    ]