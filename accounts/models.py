from uuid import uuid4

from django.conf import settings
from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractUser
# from topic.models import TopicInstance


# Create your models here.
from topic.models import Topic


class Team(models.Model):
    name = models.CharField('队伍名称', max_length=50, unique=True)
    uuid = models.CharField('队伍ID', max_length=8, unique=True, default=uuid4())
    create_time = models.DateTimeField(auto_now_add=True)

    @property
    def score(self):
        integral = 0
        members = Member.objects.filter(team=self)
        for member in members:
            integral += member.score
        return integral if integral else 0

    def __str__(self):
        return self.name


class MyUserManager(BaseUserManager):
    def create_user(self, email, username, password=None, *args, **kwargs):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            username=username,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Member(AbstractUser):
    username = models.CharField('用户名', max_length=64, unique=True)
    email = models.EmailField('邮箱', max_length=255, unique=True)
    school = models.CharField('学校', max_length=30)
    team = models.ForeignKey(Team, verbose_name="队伍", on_delete='SET_NULL', null=True, blank=True)
    is_leader = models.BooleanField('是否为队长', default=False)
    # grade = models.CharField
    # USERNAME_FIELD = 'username'
    # REQUIRED_FIELDS = ['username']
    objects = MyUserManager()

    @property
    def score(self):
        solved_problems = SolveProblem.objects.filter(member=self)
        integral = 0
        for solved_problem in solved_problems:
            integral += solved_problem.integral
        return integral if integral else 0
        # return utils.get_score_by_member(self)

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name
        ordering = ['-id']

    def __str__(self):
        return self.username


class TopicInstance(models.Model):
    # 用team_id 为空的表示为训练题目
    team = models.ForeignKey(Team, null=True, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    port = models.IntegerField('题目端口')
    flag = models.CharField('题目答案', max_length=50)
    container_id = models.CharField('容器ID', max_length=16, null=True)

    @property
    def integral(self):
        return self.topic.integral


class SolveProblem(models.Model):
    member = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="做题人", on_delete='CASCADE')
    topic = models.ForeignKey(TopicInstance, verbose_name="题目", on_delete='CASCADE')
    create_time = models.DateTimeField(auto_now_add=True)

    @property
    def integral(self):
        return self.topic.integral

    class Meta:
        unique_together = ["member", "topic"]
