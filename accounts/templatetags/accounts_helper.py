from django import template
from django.forms import BoundField
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe
from django.db import models
from django.conf import settings
from topic.models import Topic, TopicInstance
from topic.utils import getContainerStatus

register = template.Library()


@register.filter(name="form_filed", help_content=None)
def form_filed(field: BoundField):
    # type(filed)
    field.css_classes('layui-input')
    # field.build_widget_attrs({'class': "layui-input", })
    return mark_safe(field)

