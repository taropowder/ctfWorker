
from django.conf.urls import url
from topic import views as topic_views

urlpatterns = [
    url(r'/upload/', topic_views.TopicCreate.as_view(), name='topic_upload'),
    url(r'/detail/(?P<pk>\d+)/', topic_views.TopicDetailView.as_view(), name='topic_detail'),
    url(r'/list/', topic_views.TopicListView.as_view(), name='topic_list'),
    url(r'/group_list/', topic_views.TopicGroupListView.as_view(), name='topic_group_list'),
    url(r'^(.+)/', topic_views.topic, name='type'),

]
