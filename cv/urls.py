from django.conf.urls import url
from . import views

app_name='cv'
urlpatterns=[
	url(r'^$', views.IndexView.as_view(),name='index'),
	url(r'^create/$',views.CreateCV,name='create'),
	url(r'^(?P<pk>[0-9]+)/$',views.CView.as_view(),name='detail'),
]