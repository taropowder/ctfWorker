from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from django.shortcuts import render
from topic.models import Topic, TopicInstance, Team, TopicGroup
from topic.forms import UploadForm
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView, View


# Create your views here.

def home(request):
    form = UploadForm()
    return render(request, 'index.html', {'form': form})


class TopicCardView(ListView):
    template_name = 'topic/topic_card_list.html'
    model = TopicGroup

    def get_context_data(self, **kwargs):
        kwargs['type'] = self.kwargs['type']
        return super(TopicCardView, self).get_context_data(**kwargs)

    def get_queryset(self):
        qs = super(TopicCardView, self).get_queryset()
        return qs.filter(topic__type=self.kwargs['type'])

def topic(request, type):
    content = {}
    content['type'] = type
    return render(request, 'topic.html', content)


class TopicCreate(CreateView):
    model = Topic
    form_class = UploadForm  # 表类
    template_name = 'topic/topic_form.html'  # 添加表对象的模板页面
    success_url = reverse_lazy('topic_list')  # 成功添加表对象后 跳转到的页面

    def form_invalid(self, form):  # 定义表对象没有添加失败后跳转到的页面。
        return HttpResponse("form is invalid.. this is just an HttpResponse object")


class TopicListView(ListView):
    template_name = 'topic/topic_list.html'
    model = Topic


class TopicGroupListView(ListView):
    template_name = 'topic/topic_group_list.html'
    model = TopicGroup


class TopicDetailView(DetailView):
    template_name = 'topic/topic_detail.html'
    model = Topic


class TopicUpdateView(UpdateView):
    model = Topic
    form_class = UploadForm
    template_name = 'topic/topic_form.html'  # 添加表对象的模板页面

    def get_success_url(self):
        return reverse_lazy('topic_detail', kwargs=self.kwargs)


class TopicDeleteView(DeleteView):
    model = Topic
    success_url = reverse_lazy('topic_list')

    get = DeleteView.http_method_not_allowed


class TopicGroupJoinView(CreateView):
    get = View.http_method_not_allowed
    model = TopicGroup
    success_url = reverse_lazy('topic_group_list')  # 成功添加表对象后 跳转到的页面
    fields = ('topic',)

    def form_invalid(self, form):  # 定义表对象没有添加失败后跳转到的页面。
        return HttpResponse("form is invalid.. this is just an HttpResponse object")


class TopicGroupDeleteView(DeleteView):
    model = TopicGroup
    success_url = reverse_lazy('topic_group_list')

    get = DeleteView.http_method_not_allowed
