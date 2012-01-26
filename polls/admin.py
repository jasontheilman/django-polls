# -*- coding: utf-8 -*-
from django.contrib import admin
from polls.models import Poll, Answer

admin.site.register(Poll)
admin.site.register(Answer) 