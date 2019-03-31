from django.conf.urls import url, include
from django.urls import path, include
from accounts import views as accounts_views
urlpatterns = [
    url('team/create', accounts_views.TeamCreateView.as_view(), name='create_team'),
    url('team/join', accounts_views.TeamJoinView.as_view(), name='join_team'),
    url('team/detail/(?P<pk>\d+)/', accounts_views.TeamDetailView.as_view(), name='team_detail'),
    url('detail/(?P<pk>\d+)/', accounts_views.MemberDetailView.as_view(), name='account_detail'),
    url('update/(?P<pk>\d+)/', accounts_views.MemberUpdateView.as_view(), name='account_update'),
    url('check_flag/', accounts_views.solveProblemView.as_view(), name='check_flag'),
]