from django.urls import re_path
from . import views

app_name='cv'
urlpatterns=[
	 re_path(r'^$', views.IndexView.as_view(),name='index'),
	 re_path(r'^create/$',views.CreateCV,name='create'),
	 re_path(r'^(?P<pk>[0-9]+)/$',views.CView.as_view(),name='detail'),
]
