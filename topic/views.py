import os

from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.views.generic.detail import SingleObjectMixin
from django.conf import settings
from topic.models import Topic, TopicInstance, Team
from topic.forms import UploadForm
from topic import utils
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView, View
from topic import tasks


# Create your views here.

def home(request):
    form = UploadForm()
    return render(request, 'index.html', {'form': form})


class TopicCardView(ListView):
    if settings.RUNNING_MODEL == 'training':
        template_name = 'topic/topic_card_list_training.html'

    model = Topic

    def get_context_data(self, **kwargs):
        kwargs['type'] = self.kwargs['type']
        return super(TopicCardView, self).get_context_data(**kwargs)

    def get_queryset(self):
        qs = super(TopicCardView, self).get_queryset()
        return qs.filter(type=self.kwargs['type']).filter(in_group=True)


# def topic(request, type):
#     content = {}
#     content['type'] = type
#     return render(request, 'topic.html', content)


class TopicCreate(CreateView):
    model = Topic
    form_class = UploadForm  # 表类
    template_name = 'topic/topic_form.html'  # 添加表对象的模板页面
    success_url = reverse_lazy('topic_list')  # 成功添加表对象后 跳转到的页面

    def form_valid(self, form):
        self.object = form.save()
        utils.un_zip(self.object.zip_file.path, self.object.build_name)
        return super(TopicCreate, self).form_valid(form)

    def form_invalid(self, form):  # 定义表对象没有添加失败后跳转到的页面。
        return HttpResponse("form is invalid.. this is just an HttpResponse object")


class TopicListView(ListView):
    template_name = 'topic/topic_list.html'
    model = Topic


class TopicGroupListView(ListView):
    template_name = 'topic/topic_group_list.html'
    model = Topic

    def get_queryset(self):
        qs = super(TopicGroupListView, self).get_queryset()
        return qs.filter(in_group=True)

class TopicDetailView(DetailView):
    template_name = 'topic/topic_detail.html'
    model = Topic


class TopicUpdateView(UpdateView):
    model = Topic
    form_class = UploadForm
    template_name = 'topic/topic_form.html'  # 添加表对象的模板页面

    def get_success_url(self):
        return reverse_lazy('topic_detail', kwargs=self.kwargs)

    def form_valid(self, form):
        form.empty_permitted =True
        self.object = form.save()
        utils.un_zip(self.object.zip_file.path, self.object.build_name)
        return HttpResponseRedirect(self.get_success_url())


class TopicDeleteView(DeleteView):
    model = Topic
    success_url = reverse_lazy('topic_list')

    get = DeleteView.http_method_not_allowed


class TopicGroupJoinView(UpdateView):
    get = View.http_method_not_allowed
    model = Topic
    success_url = reverse_lazy('topic_group_list')  # 成功添加表对象后 跳转到的页面
    fields = ('in_group',)

    def form_invalid(self, form):  # 定义表对象没有添加失败后跳转到的页面。
        return HttpResponse("form is invalid.. this is just an HttpResponse object")


class TopicGroupDeleteView(UpdateView):
    model = Topic
    success_url = reverse_lazy('topic_group_list')
    fields = ('in_group',)
    get = DeleteView.http_method_not_allowed

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        utils.removeContainerFromDockerFile(self.object.id)
        return super(TopicGroupDeleteView, self).post(request, *args, **kwargs)


class buildImageView(View):
    get = View.http_method_not_allowed

    def post(self, request):
        message = "已开始BUILD"
        id = request.POST.get('topic', None)
        if id:
            result = tasks.build_images.delay(id)
            # TODO: 检查是否加入BUILD队列
            # if result.ready():
            #     message = "已经开始BUILD"
            #     # print("Task has run")
            #     if result.successful():
            #         print("Result was: %s" % result.result)
            #     else:
            #         if isinstance(result.result, Exception):
            #             print("Task failed due to raising an exception")
            #             raise result.result
            #         else:
            #             print("Task failed without raising exception")
            # else:
            #     message = "未build，请检查celery服务是否开启"
            return HttpResponse(message)
        else:
            return HttpResponse("ID错误")


class ImagesBuildLogs(SingleObjectMixin, View):
    model = Topic

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return HttpResponse(self.object.build_log)


class TopicInstanceListView(ListView):
    template_name = 'topic/topicinstance_list.html'
    model = Topic

    def get_queryset(self):
        qs = super(TopicInstanceListView, self).get_queryset()
        return qs.filter(in_group=True)


class TopicGroupStartView(View):

    def post(self, request):
        topic_group = Topic.objects.filter(in_group=True)
        result = []
        for topic in topic_group:
            if topic.build_status == 'success':
                if topic.build_type == 'Dockerfile':
                    if not TopicInstance.objects.filter(topic=topic).first():
                        result.append(utils.runContainerFromDockerFile(topic))

        return JsonResponse(result, safe=False)


