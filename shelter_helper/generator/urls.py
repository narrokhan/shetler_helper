from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<passport_no> [-\w]+)/$', views.detail, name='detail'),
]