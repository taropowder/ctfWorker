from django import template
from django.urls import reverse_lazy
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe
from django.db import models
from django.conf import settings
from topic.models import Topic, TopicType
from accounts.models import TopicInstance
from topic.utils import getContainerStatus

register = template.Library()


@register.filter(name="filed", help_content=None)
def fill_form_filed(filed, help_content=None):
    if help_content:
        filed_label = """
         <div class="layui-form-item">
                        <label class="layui-form-label">{label}</label>
                        <div class="layui-input-inline">
                                                     {input} 
                        </div>
                    <div class="layui-form-mid layui-word-aux">{help}</div>
                    </div>
        """
    else:
        filed_label = """
                <div class="layui-form-item">
                        <label class="layui-form-label">{label}</label>
                        <div class="layui-input-inline">
                                                     {input} 
                        </div>
                    </div>
                """
    # if autoescape:
    #     name = conditional_escape(filed)
    return mark_safe(filed_label.format(label=filed.label, input=filed, help=help_content))


@register.filter(name="select", help_content=None)
def fill_form_filed(filed, help_content=None):
    if help_content:
        filed_label = """
         <div class="layui-form-item">
                        <label class="layui-form-label">{label}</label>
                        <div class="layui-input-block">

                                                     {input} 
                        </div>
                    <div class="layui-form-mid layui-word-aux">{help}</div>
                    </div>
        """
    else:
        filed_label = """
                <div class="layui-form-item">
                        <label class="layui-form-label">{label}</label>
                        <div class="layui-input-block">

                                                     {input} 
                        </div>
                    </div>
                """
    # if autoescape:
    #     name = conditional_escape(filed)
    return mark_safe(filed_label.format(label=filed.label, input=filed, help=help_content))


@register.filter(name="detail_filed", filed=None)
def fill_form_filed(model: models.Model, field=None):
    filed_label = """
                <tr>
                    <td>{label}</td>
                    <td>{value}</td>
                </tr>
                """

    return mark_safe(filed_label.format(label=model._meta.get_field(field).verbose_name, value=getattr(model, field)))


@register.filter(name="detail_select_filed", filed=None)
def fill_form_filed(model: models.Model, field=None):
    filed_label = """
                <tr>
                    <td>{label}</td>
                    <td>{value}</td>
                </tr>"""
    # getattr(models, 'get_' + field + '_display'))
    return mark_safe(filed_label.format(label=model._meta.get_field(field).verbose_name,
                                        value=eval(f'model.get_{field}_display()')))


@register.filter(name="url_parser", filed=None)
def fill_form_filed(host: str, topic: Topic):
    if ':' in host:
        host = host.split(':')[0]
    if settings.RUNNING_MODEL == 'training':
        # 其他方式类型题目补充： 如只有URL方式
        instance = TopicInstance.objects.filter(topic=topic).first()
        if not instance:
            return ""
        else:
            port = instance.port
        url = f"http://{host}:{port}"
    return mark_safe(url)


@register.filter(name="instance_filter")
def get_topic_instance(topic: Topic):
    instances = TopicInstance.objects.filter(topic=topic.id)
    if topic.build_type == 'Dockerfile':
        html_header = f"""
                 <div class="layui-colla-item">
                                <h2 class="layui-colla-title">{topic.title}</h2>
                                <div class="layui-colla-content">
                                    <table class="layui-table" lay-skin="line">
                                        <thead>
                                        <th>题目端口</th>
                                        <th>题目队伍</th> 
                                        <th>容器ID</th> 
                                        <th>容器状态</th>
                                        </thead>
                                        <tbody>
        """
        html_body_templates = """
        <tr>
        <td>{port}</td>
        <td>{team}</td>
        <td>{id}</td>
        <td>{status}</td>
        </tr>
        """
    html_body = ""
    for instance in instances:
        if instance.team:
            team = instance.team.name
        else:
            team = "ALL"
        html_body += html_body_templates.format(port=instance.port, team=team, id=instance.container_id,
                                                status=getContainerStatus(instance.container_id))
    html_footer = """
    </tbody>

                                </table>
                            </div>
                        </div>
    """

    return mark_safe(html_header + html_body + html_footer)


@register.filter(name="card_show_training")
def card_show():
    html = """
     <div class="layui-col-md4">
                    <a href="#">
                        <div class="layui-card"
                             onclick="showTopic('{{ request.get_host | url_parser:topicgroup.topic.port }}','{{ topicgroup.topic.title }}')">
                            <div class="layui-card-header">{{ topicgroup.topic.title }}</div>
                            <div class="layui-card-body">
                                {{ topicgroup.topic.introduction }}
                            </div>
                        </div>
                    </a>

                </div>"""


@register.simple_tag
def type_li():
    types = TopicType.objects.all()
    lis = ""
    for topic_type in types:

        lis += f"""<dd><a href="{reverse_lazy('show_topics_with_type', kwargs={'type': topic_type })}">{topic_type}</a></dd>"""
    return mark_safe(lis)
