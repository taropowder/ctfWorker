from allauth.account.forms import LoginForm, PasswordField, SignupForm
from django import forms
from django.forms import widgets, Field

from accounts.models import Team
from .models import Member, SolveProblem


# Field.default_error_messages = {
#
# }

class MySignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super(MySignupForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget = forms.TextInput(attrs={'class': 'layui-input'})
        self.fields['username'].widget = forms.TextInput(attrs={'class': 'layui-input'})
        self.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'layui-input'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'layui-input'})
        self.fields['password2'].label = "重复密码"


class MyLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super(MyLoginForm, self).__init__(*args, **kwargs)
        self.fields['password'].widget = forms.PasswordInput(attrs={'class': 'layui-input'})
        self.fields['login'].widget = forms.TextInput(attrs={'class': 'layui-input'})


class UserForm(forms.ModelForm):
    # username = forms.CharField(widget=widgets.TextInput(attrs={'class': 'layui-input'}))

    class Meta:
        model = Member
        widgets = {
            'username': widgets.TextInput(attrs={'class': 'layui-input'}),
            'school': widgets.TextInput(attrs={'class': 'layui-input'}),
        }
        fields = [
            'username',
            'school',
        ]


class SolveProblemForm(forms.ModelForm):
    flag = forms.CharField()

    class Meta:
        model = SolveProblem
        fields = {
            'topic',
        }


class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        widgets = {
            'name': widgets.TextInput(attrs={'class': 'layui-input'}),
        }
        fields = {
            'name'
        }


class JoinTeamForm(forms.Form):
    uuid = forms.UUIDField(
        label='队伍UUID',
        widget=widgets.TextInput(attrs={'class': 'layui-input'}),
    )

    name = forms.CharField(
        label='队伍名称',
        widget=widgets.TextInput(attrs={'class': 'layui-input'}),
    )

    # def clean_uuid(self):
    #     team = Team.objects.filter(uuid=self.cleaned_data['uuid']).filter(name=self.cleaned_data['name']).first()
    #     raise forms.ValidationError('上传的文件类型不被允许')
