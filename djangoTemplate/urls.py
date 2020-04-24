from django.conf.urls import url
from djangoTemplate import views

urlpatterns = [
    url(r'^$', views.HomePageView, name='index'),
]