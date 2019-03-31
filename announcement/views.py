from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from announcement.models import Announcement


class AnnouncementListView(ListView):
    template_name = 'announcement/announcement_list.html'
    model = Announcement


