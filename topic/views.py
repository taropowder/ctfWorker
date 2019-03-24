from django.db import IntegrityError
from django.http import HttpResponse
from django.shortcuts import render
from topic.models import Topic, TopicInstance, Team
from topic.forms import UploadForm
from django.views.generic import CreateView, ListView


# Create your views here.

def home(request):
    form = UploadForm()
    return render(request, 'index.html', {'form': form})


def topic(request, type):
    print(type)
    content = {}
    content['type'] = type
    return render(request, 'topic.html', content)


def upload(request):
    content = {}
    if request.method == 'GET':
        content['deploy_types'] = Topic.BUILD_TYPE_CHOOSE
        content['topic_types'] = Topic.TYPE_CHOOSE
        content['form'] = UploadForm()
        return render(request, 'upload.html', content)


class TopicCreate(CreateView):
    model = Topic
    form_class = UploadForm  # 表类
    template_name = 'upload.html'  # 添加表对象的模板页面
    success_url = '/'  # 成功添加表对象后 跳转到的页面

    def form_invalid(self, form):  # 定义表对象没有添加失败后跳转到的页面。
        print(form.errors)
        return HttpResponse("form is invalid.. this is just an HttpResponse object")

class TopicListView(ListView):
    template_name = 'topic/topoc_list.html'
    model = Topic

