from django import forms
from django.forms import widgets
from .models import Topic


class UploadForm(forms.ModelForm):
    empty_permitted = True
    port = forms.IntegerField(
        label="映射端口",
        widget=widgets.NumberInput(attrs={'class': "layui-input", 'placeholder': '0-65535'})
    )

    type = forms.CharField(
        label='赛题类型',
        widget=forms.Select(choices=Topic.TYPE_CHOOSE, attrs={'lay-verify': 'required'})
    )

    build_type = forms.CharField(
        widget=forms.Select(choices=Topic.BUILD_TYPE_CHOOSE, attrs={'lay-verify': 'required'})
    )

    title = forms.CharField(
        label='题目名称',
        widget=forms.TextInput(attrs={'class': "layui-input"})
    )
    introduction = forms.CharField(
        label='题目介绍',
        widget=forms.Textarea(attrs={'class': "layui-textarea", 'rows': '5'})
    )
    build_name = forms.CharField(
        label='镜像名称',
        widget=forms.TextInput(attrs={'class': "layui-input"})
    )
    exec_command = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': "layui-input"})
    )

    zip_file = forms.FileField(
        label='部署文件',
        required=True
    )

    def clean_zip_file(self):
        exts = ['zip', '7z']
        for ext in exts:
            if self.cleaned_data['zip_file'].name.endswith(ext):
                return self.cleaned_data['zip_file']
        raise forms.ValidationError('上传的文件类型不被允许')

    class Meta:
        model = Topic
        fields = [
            'port',
            'type',
            'zip_file',
            'build_type',
            'title',
            'introduction',
            'build_name',
            'exec_command',
            'flag_is_unique',
        ]
