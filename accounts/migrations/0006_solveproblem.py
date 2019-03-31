# Generated by Django 2.1.7 on 2019-03-30 12:21

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topic', '0005_auto_20190330_1221'),
        ('accounts', '0005_member_team'),
    ]

    operations = [
        migrations.CreateModel(
            name='SolveProblem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member', models.ForeignKey(on_delete='CASCADE', to=settings.AUTH_USER_MODEL, verbose_name='做题人')),
                ('topic', models.ForeignKey(on_delete='CASCADE', to='topic.TopicInstance', verbose_name='题目')),
            ],
        ),
    ]