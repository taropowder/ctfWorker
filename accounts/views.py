from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .forms import UserForm
# Create your views here.
from django.views.generic import DetailView, UpdateView
from django.urls import reverse_lazy

from accounts.models import Member


class MemberDetailView(DetailView):
    template_name = 'accounts/accounts_detail.html'
    model = Member


class MemberUpdateView(UpdateView):
    template_name = 'accounts/accounts_form.html'
    model = Member
    form_class = UserForm

    def get_success_url(self):
        return reverse_lazy('account_detail', kwargs=self.kwargs)
        # fields = ('username', 'school')
