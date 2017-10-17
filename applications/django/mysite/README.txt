######################################################
Model
######################################################
polls:
	models.Question
	models.Choice

######################################################
View
######################################################
polls:
	views.index
	views.detail
	views.results
	views.vote
	views.IndexView
	views.DetailView
	views.ResultView

######################################################
URL
######################################################
polls:
	# 定义URL名称的命名空间
	# 用法ex: 'polls:detail'
	app_name = "polls"
	urlpatterns = [
	    # ex: /polls/
	    # url(r'^$', views.index, name = "polls_index"),
	    # 使用通用视图
	    url(r'^$', views.IndexView.as_view(), name = "index"),
	    # 命名捕获组, 用于向视图函数传入参数
	    # ex: /polls/5
	    # url(r'^(?P<question_id>[0-9]+)/$', views.detail, name = "detail"),
	    # 使用通用视图
	    # except: Generic detail view DetailView must be called with either an object pk or a slug.
	    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name = "detail"),
	    # ex: /polls/5/results/
	    # url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name = "results"),
	    # 使用通用视图
	    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultView.as_view(), name = "results"),
	    # ex: /polls/5/vote/
	    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name = "vote"),
	]

######################################################
Template
######################################################
polls:
	detail.html
	index.html
	results.html

