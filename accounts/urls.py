from django.conf.urls import url
from django.urls import path, include
from accounts import views as accounts_views
urlpatterns = [
    url('/detail/(?P<pk>\d+)/', accounts_views.MemberDetailView.as_view(), name='account_detail'),
]