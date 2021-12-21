from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^simple_route\w{0,}', views.simple_route, name='simple_route'),
    url(r'^slug_route/((?P<page_slug>.{1,})/)*', views.slug_route, name='slug_route'),
    
    url('sum_route/(?P<a>\S+)/(?P<b>\S+)/$', views.sum_route, name='sum_route'),
    url(r'sum_get_method/', views.sum_get_method, name = 'sum_get_method'),
    url(r'sum_post_method/', views.sum_post_method, name = 'sum_post_method'),

]

