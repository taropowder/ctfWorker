from django.db import IntegrityError
from django.http import HttpResponse
from django.shortcuts import render
from topic.models import Topic, TopicInstance, Team, TopicGroup
from topic.forms import UploadForm
from django.views.generic import CreateView, ListView, DetailView


# Create your views here.

def home(request):
    form = UploadForm()
    return render(request, 'index.html', {'form': form})


def topic(request, type):
    content = {}
    content['type'] = type
    return render(request, 'topic.html', content)


class TopicCreate(CreateView):
    model = Topic
    form_class = UploadForm  # 表类
    template_name = 'upload.html'  # 添加表对象的模板页面
    success_url = '/'  # 成功添加表对象后 跳转到的页面

    def form_invalid(self, form):  # 定义表对象没有添加失败后跳转到的页面。
        return HttpResponse("form is invalid.. this is just an HttpResponse object")


class TopicListView(ListView):
    template_name = 'topic/topoc_list.html'
    model = Topic


class TopicGroupListView(ListView):
    template_name = 'topic/topocgroup_list.html'
    model = TopicGroup


class TopicDetailView(DetailView):
    template_name = 'topic/topic_detail.html'
    model = Topic
