# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Question, Choice

# 注册到admin管理页面中
admin.site.register(Question)
admin.site.register(Choice)