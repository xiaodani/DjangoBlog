
from django.conf.urls import url
from . import views

app_name = 'articles'

# url pattern read in order!
urlpatterns = [
    url(r'^$', views.article_list, name="list"),
    url(r'^create/$', views.article_create, name="create"),
    url(r'^(?P<id>[\d*]+)/$', views.article_detail, name="detail"),
]
