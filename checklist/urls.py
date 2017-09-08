from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^checklist1', views.checklist1, name='checklist1'),
    url(r'^checklist2', views.checklist2, name='checklist2'),
    url(r'^checklist3', views.checklist3, name='checklist3'),
]
