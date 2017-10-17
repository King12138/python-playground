# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone
import datetime

# 定义应用中数据模型

class Question(models.Model):
    question_text = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        """是否是近期发布的"""
        # return self.pub_date >= timezone.now() - datetime.timedelta(days = 1)
        now = timezone.now()
        return now - datetime.timedelta(days = 1) <= self.pub_date <= now

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete = models.CASCADE)  # 外键定义
    choice_text = models.CharField(max_length = 200)
    votes = models.IntegerField(default = 0)

    def __str__(self):
        return self.choice_text
