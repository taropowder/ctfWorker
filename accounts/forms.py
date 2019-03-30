from allauth.account.forms import LoginForm, PasswordField, SignupForm
from django import forms
from .models import Member


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
    class Meta:
        model = Member
        fields = [
            'username',
            'team',
        ]