from django.conf.urls import url

from . import views

app_name = 'filebrowser'
urlpatterns = [
    url(r'^$', views.dirindex, name='dirindex'),
]
