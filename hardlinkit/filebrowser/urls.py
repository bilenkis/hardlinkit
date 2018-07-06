from django.conf.urls import url

from . import views

app_name = 'filebrowser'
urlpatterns = [
    url(r'^$', views.start, name='start'),
    url(r'^dirindex/', views.dirindex, name='dirindex'),
    url(r'^dirindex/filebrowser/', views.filebrowser, name='filebrowser'),

]
