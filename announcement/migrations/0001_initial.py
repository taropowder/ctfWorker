# Generated by Django 2.1.7 on 2019-03-31 09:21

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Anncouncement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='内容')),
                ('create_time', models.DateTimeField(auto_now=True, verbose_name='创建时间')),
                ('title', models.CharField(max_length=50, verbose_name='标题')),
                ('admin', models.ForeignKey(on_delete='PROTECT', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-create_time'],
            },
        ),
    ]
