from allauth.account.forms import LoginForm, PasswordField, SignupForm
from django import forms
from django.forms import widgets, Field

from topic.models import Team
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
            'team',
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
