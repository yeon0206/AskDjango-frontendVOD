from django.conf.urls import include, url
from . import views
urlpatterns=[
    url(r'^$', views.index, name='index'),
    url(r'^new/$', views.post_new, name='post_new'),
    url(r'^(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^(?P<pk>\d+)/delete/$', views.post_delete, name='post_delete'),

    url(r'^(?P<post_pk>\d+)/comments/new/$', views.comment_new, name='comment_new'),
    url(r'^(?P<post_pk>\d+)/comments/(?P<pk>\d+)/edit/$', views.comment_edit, name='comment_edit'),
    url(r'^(?P<post_pk>\d+)/comments/(?P<pk>\d+)/delete/$', views.comment_delete, name='comment_delete'),

    url(r'^posts\.json$', views.post_list_json), # 직렬화 테스트

    url(r'^api/v1/', include('blog.api')),
]