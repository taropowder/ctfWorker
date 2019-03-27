from django import template
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe
from django.db import models

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
def fill_form_filed(host:str, port=None):
    if ':' in host:
        host = host.split(':')[0]
    if port:
        url = f"http://{host}:{port}"
    else:
        url = f"http://{host}"
    # getattr(models, 'get_' + field + '_display'))
    return mark_safe(url)
