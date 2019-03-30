from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.views.generic import DetailView

from accounts.models import Member


class MemberDetailView(DetailView):
    template_name = 'accounts/accounts_detail.html'
    model = Member