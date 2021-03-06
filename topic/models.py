from django.conf import settings
from django.db import models
from uuid import uuid1, uuid4
# from accounts.models import Team

# Create your models here.


class TopicType(models.Model):
    name = models.CharField("类型", max_length=60)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "类型"

class Topic(models.Model):
    TYPE_CHOOSE = (
        ('bin', '二进制'),
        ('web', 'web安全'),
        ('misc', '杂项'),
        ('pwn', 'PWN'),
    )
    BUILD_TYPE_CHOOSE = (
        ('Dockerfile', 'Dockerfile'),
        ('DockerCompose', 'DockerCompose'),
    )
    BUILD_STATUS_CHOOSE = (
        ('ready', '未BUILD'),
        ('building', '正在build'),
        ('success', 'build成功'),
        ('fail', 'build失败'),
    )
    build_status = models.CharField('BUILD状态', choices=BUILD_STATUS_CHOOSE, default='ready', max_length=20)
    build_log = models.TextField('BUILD日志', null=True)
    # path = models.CharField('Dockerfile/docker-compose.yml文件路径', max_length=60)
    port = models.IntegerField('需要映射出来的端口')
    build_type = models.CharField('Build方式', choices=BUILD_TYPE_CHOOSE, max_length=20)
    title = models.CharField('题目名称', max_length=60)
    build_name = models.CharField('英文名称', max_length=80)
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    type = models.ForeignKey(TopicType,verbose_name='题目类型',on_delete='PROTECT')
    # type = models.CharField('题目类型', choices=TYPE_CHOOSE, max_length=20)
    introduction = models.TextField('题目简介')
    flag_is_unique = models.BooleanField('答案是否唯一')
    exec_command = models.TextField('需要执行的命令', null=True)
    zip_file = models.FileField(verbose_name='部署的压缩包', upload_to=f'docker/{uuid4()}', null=False)
    image_id = models.CharField('镜像ID', null=True, max_length=16)
    in_group = models.BooleanField("是否加入试卷", default=False)
    flag = models.CharField('FLAG', max_length=50, null=True)
    integral = models.IntegerField('积分', default=0)


