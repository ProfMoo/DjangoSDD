from django.conf.urls import url
from . import views

app_name = 'polls'
urlpatterns = [
	#ex: /polls/
	url(r'^$', views.IndexView.as_view(), name='index'), ##assigning this url to the view index
	#ex: /polls/5/
	url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'), ##assigning this url to the view detail
	#ex: /polls/5/results/
	url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'), ##assigning this url to the view results
	#ex: /polls/5/vote/
	url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'), ##assigning this url to the view vote
	#ex: /polls/ayylmao
	url(r'^ayylmao/$', views.AyyLmao.as_view(), name='ayylmao'),
]