# Generated by Django 2.1.7 on 2019-03-31 06:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_member_is_leader'),
    ]

    operations = [
        migrations.AddField(
            model_name='solveproblem',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]