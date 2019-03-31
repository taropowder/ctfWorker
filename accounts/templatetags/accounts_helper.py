from django import template
from django.db.models import Sum
from django.forms import BoundField
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe
from django.db import models
from django.conf import settings

from accounts.models import Member, SolveProblem
from accounts.utils import get_score_by_member
from topic.models import Topic, TopicInstance
from topic.utils import getContainerStatus

register = template.Library()


@register.filter(name="form_filed", help_content=None)
def form_filed(field: BoundField):
    # type(filed)
    field.css_classes('layui-input')
    # field.build_widget_attrs({'class': "layui-input", })
    return mark_safe(field)


@register.filter(name="is_solved", help_content=None)
def is_solved(topic: Topic, member: Member):
    result = ""
    if SolveProblem.objects.filter(topic__topic=topic).filter(member=member).first():
        result = 'style="background-color: #858585"'
    return mark_safe(result)


@register.filter(name="get_score")
def get_score(member: Member):
    integral = get_score_by_member(member)
    return mark_safe(integral)
