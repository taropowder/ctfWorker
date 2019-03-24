from django import template
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe

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
