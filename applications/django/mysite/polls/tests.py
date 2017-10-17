# -*- coding: utf-8 -*-
from django.test import TestCase
from django.utils import timezone

# 创建测试

from .models import Question, Choice
import datetime
from django.urls import reverse


######################################################
# 测试模型
######################################################
class QuestionModelTest(TestCase):

    def test_was_published_recently_with_future_question(self):
         """测试计划于未来发布的问题"""
         import datetime
         future_time = timezone.now() + datetime.timedelta(days = 30)
         future_question = Question(pub_date = future_time)
         self.assertIs(future_question.was_published_recently(), False, "未来发布的问题不应该属于最近发布的问题.")


######################################################
# 测试视图
######################################################

def create_question(question_text, days):
    """辅助函数: 创建问题"""
    time = timezone.now() + datetime.timedelta(days = days)
    return Question.objects.create(question_text = question_text, pub_date = time)

class QuestionIndexViewTest(TestCase):
    def test_no_question(self):
        response = self.client.get(reverse("polls:index"))  # 使用客户端
        #print(response)
        self.assertEqual(response.status_code, 200)  # 响应码
        self.assertContains(response, "No polls are available.")  # 响应中内容
        self.assertQuerysetEqual(response.context["latest_question_list"], [])  # 响应中上下文

    def test_single_question(self):
        create_question("A dummy question", days = 1)
        response = self.client.get(reverse("polls:index"))
        #print(response.context)
        self.assertQuerysetEqual(response.context["latest_question_list"], ["<Question: A dummy question>"])
