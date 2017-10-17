# -*- coding: utf-8 -*-
from django.http import HttpResponse, Http404
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Question, Choice


######################################################
# 定义视图函数
######################################################
def index(request):
    """polls应用首页"""
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {"latest_question_list": latest_question_list}
    # 原生方式
#     from django.template import loader
#     template = loader.get_template("polls/index.html")
#     return HttpResponse(template.render(context, request))
    # 快捷方式
    return render(request, "polls/index.html", context)

def detail(request, question_id):
    """问题详情页"""
#     return HttpResponse("You are looking at question %s." % question_id)
#     try:
#         question = Question.objects.get(pk = question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question " + question_id + " does not exist")
    question = get_object_or_404(Question, pk = question_id)  # 快捷方式
    return render(request, "polls/detail.html", {"question": question})


def results(request, question_id):
    """问题的结果页"""
#     response = "You are looking at the results of question %s."
#     return HttpResponse(response % question_id)
    question = get_object_or_404(Question, pk = question_id)
    return render(request, "polls/results.html", {"question": question})

def vote(request, question_id):
    """问题的投票页"""
    # TODO(zhoujiagen) 事务如何处理???
#     return HttpResponse("You are voting on question %s." % question_id)
    question = get_object_or_404(Question, pk = question_id)
    try:
        selected_choice = question.choice_set.get(pk = request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        context = {
            "question": question,
            "error_message": "You didn't select a choice." }
        return render(request, "polls/detail.html", context)
    else:
        selected_choice.votes += 1
        selected_choice.save()  # 保存
        # 重定向
        # reverse: 由URL名称获取视图路径, 参数: URL名称, 参数
        return HttpResponseRedirect(
            reverse("polls:results", args = (question.id,)))


######################################################
# 定义通用视图
######################################################

class IndexView(generic.ListView):
    """polls应用首页-通用视图"""
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"  # 默认Context对象名称为question_list

    def get_queryset(self):
        """返回最近的问题"""
        # filter: 过滤
        return Question.objects.filter(pub_date__lte = timezone.now()).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    """问题详情-通用视图"""
    model = Question  # 默认Context对象名称为question
    template_name = "polls/detail.html"

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte = timezone.now())

class ResultView(generic.DetailView):
    """结果-通用视图"""
    model = Question  # 默认Context对象名称为question
    template_name = "polls/results.html"











