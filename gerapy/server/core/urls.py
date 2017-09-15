from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^api/client/$', views.client_index, name='client_index'),
    url(r'^api/client/create', views.client_create, name='client_create'),
    url(r'^api/client/(\d+)/$', views.client_show, name='client_show'),
    url(r'^api/client/(\d+)/status', views.client_status, name='client_status'),
    url(r'^api/client/(\d+)/update', views.client_update, name='client_update'),
    url(r'^api/client/(\d+)/remove', views.client_remove, name='client_remove'),
    url(r'^api/client/(\d+)/projects/$', views.project_list, name='project_list'),
    url(r'^api/client/(\d+)/project/(\S+)/spiders/$', views.spider_list, name='spider_list'),
    url(r'^api/client/(\d+)/project/(\S+)/spider/(\S+)/job/(\S+)/log', views.job_log, name='job_log'),
    url(r'^api/client/(\d+)/project/(\S+)/spider/(\S+)/$', views.spider_start, name='spider_start'),
    url(r'^api/client/(\d+)/project/(\S+)/jobs/$', views.job_list, name='job_list'),
    url(r'^api/client/(\d+)/project/(\S+)/versions/$', views.project_versions, name='project_versions'),
    url(r'^api/client/(\d+)/project/(\S+)/deploy/$', views.project_deploy, name='project_deploy'),
    url(r'^api/client/(\d+)/project/(\S+)/job/(\S+)/cancel$', views.job_cancel, name='job_cancel'),
    url(r'^api/project/index/$', views.project_index, name='project_index'),
    url(r'^api/project/(\S+)/build', views.project_build, name='project_build'),
    url(r'^api/project/(\S+)/tree', views.project_tree, name='project_tree'),
    url(r'^api/project/(\S+)/remove', views.project_remove, name='project_remove'),
    url(r'^api/project/file/rename', views.project_file_rename, name='project_file_rename'),
    url(r'^api/project/file/delete', views.project_file_delete, name='project_file_delete'),
    url(r'^api/project/file/create', views.project_file_create, name='project_file_create'),
    url(r'^api/project/file/update', views.project_file_update, name='project_file_update'),
    url(r'^api/project/file', views.project_file, name='project_file'),
]
