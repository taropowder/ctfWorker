# Generated by Django 2.1.7 on 2019-03-31 07:31

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('topic', '0008_auto_20190331_0608'),
        ('accounts', '0009_solveproblem_create_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='队伍名称')),
                ('uuid', models.CharField(default=uuid.UUID('d6461f9c-0793-44af-b2b9-a45f14a642a2'), max_length=8, unique=True, verbose_name='队伍ID')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='TopicInstance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('port', models.IntegerField(verbose_name='题目端口')),
                ('flag', models.CharField(max_length=50, verbose_name='题目答案')),
                ('container_id', models.CharField(max_length=16, null=True, verbose_name='容器ID')),
                ('team', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.Team')),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='topic.Topic')),
            ],
        ),
        migrations.AlterField(
            model_name='member',
            name='team',
            field=models.ForeignKey(blank=True, null=True, on_delete='SET_NULL', to='accounts.Team', verbose_name='队伍'),
        ),
        migrations.AlterField(
            model_name='solveproblem',
            name='topic',
            field=models.ForeignKey(on_delete='CASCADE', to='accounts.TopicInstance', verbose_name='题目'),
        ),
    ]