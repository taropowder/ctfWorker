
from django.conf.urls import url
from topic import views as topic_views

urlpatterns = [
    url('/upload/', topic_views.TopicCreate.as_view(), name='topic_upload'),
    url('/detail/(?P<pk>\d+)/', topic_views.TopicDetailView.as_view(), name='topic_detail'),
    url('/delete/(?P<pk>\d+)/', topic_views.TopicDeleteView.as_view(), name='topic_delete'),
    url('/update/(?P<pk>\d+)/', topic_views.TopicUpdateView.as_view(), name='topic_update'),
    url('/list/', topic_views.TopicListView.as_view(), name='topic_list'),
    url('/group_list/', topic_views.TopicGroupListView.as_view(), name='topic_group_list'),
    url('/group_add/(?P<pk>\d+)/', topic_views.TopicGroupJoinView.as_view(), name='topic_group_add'),
    url('/build/', topic_views.buildImageView.as_view(), name='image_build'),
    url('/group_delete/(?P<pk>\d+)/', topic_views.TopicGroupDeleteView.as_view(), name='topic_group_delete'),
    url('/build_logs/(?P<pk>\d+)/', topic_views.ImagesBuildLogs.as_view(), name='build_logs'),
    url('/start_all/', topic_views.TopicGroupStartView.as_view(), name='start_all'),
    url('/instance_list/', topic_views.TopicInstanceListView.as_view(), name='instance_list'),
    url('/(?P<type>[\u4e00-\u9fa5_a-zA-Z0-9]+)/', topic_views.TopicCardView.as_view(), name='show_topics_with_type'),



]
