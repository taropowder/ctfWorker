from django.conf import settings
from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractUser
from topic.models import Team, TopicInstance


# Create your models here.


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
    # grade = models.CharField
    # USERNAME_FIELD = 'username'
    # REQUIRED_FIELDS = ['username']
    objects = MyUserManager()

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name
        ordering = ['-id']

    def __str__(self):
        return self.username


class SolveProblem(models.Model):
    member = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="做题人", on_delete='CASCADE')
    topic = models.ForeignKey(TopicInstance, verbose_name="题目", on_delete='CASCADE')

    class Meta:
        unique_together = ["member", "topic"]