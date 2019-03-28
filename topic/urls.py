
from django.conf.urls import url
from topic import views as topic_views

urlpatterns = [
    url(r'/upload/', topic_views.TopicCreate.as_view(), name='topic_upload'),
    url(r'/detail/(?P<pk>\d+)/', topic_views.TopicDetailView.as_view(), name='topic_detail'),
    url(r'/delete/(?P<pk>\d+)/', topic_views.TopicDeleteView.as_view(), name='topic_delete'),
    url(r'/update/(?P<pk>\d+)/', topic_views.TopicUpdateView.as_view(), name='topic_update'),
    url(r'/list/', topic_views.TopicListView.as_view(), name='topic_list'),
    url(r'/group_list/', topic_views.TopicGroupListView.as_view(), name='topic_group_list'),
    url(r'/group_add/', topic_views.TopicGroupJoinView.as_view(), name='topic_group_add'),
    url(r'/build/', topic_views.buildImageView.as_view(), name='image_build'),
    url(r'/group_delete/(?P<pk>\d+)/', topic_views.TopicGroupDeleteView.as_view(), name='topic_group_delete'),
    url(r'^/(?P<type>[A-Za-z0-9]+)/', topic_views.TopicCardView.as_view(), name='type'),

]
