from django import forms
from django.forms import widgets
from .models import Topic


class UploadForm(forms.ModelForm):
    port = forms.IntegerField(
        label="映射端口",
        widget=widgets.NumberInput(attrs={'class': "layui-input", 'placeholder': '0-65535'})
    )

    type = forms.CharField(
        label='赛题类型',
        widget=forms.Select(choices=Topic.TYPE_CHOOSE,attrs={'lay-verify': 'required'})
    )

    build_type = forms.CharField(
        widget=forms.Select(choices=Topic.BUILD_TYPE_CHOOSE,attrs={'lay-verify': 'required'})
    )

    title = forms.CharField(
        label='题目名称',
        widget=forms.TextInput(attrs={'class': "layui-input"})
    )
    introduction = forms.CharField(
        label='题目介绍',
        widget=forms.Textarea(attrs={'class': "layui-textarea",'rows': '5'})
    )
    build_name = forms.CharField(
        label='镜像名称',
        widget=forms.TextInput(attrs={'class': "layui-input"})
    )
    exec_command = forms.CharField(
        widget=forms.TextInput(attrs={'class': "layui-input"})
    )


    class Meta:
        model = Topic
        fields = [
            'port',
            'type',
            'build_type',
            'title',
            'introduction',
            'build_name',
            'exec_command',
            'flag_is_unique',
        ]
