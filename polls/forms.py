# -*- coding: utf-8 -*-
from django import forms
import datetime
from django.contrib.sites.models import Site
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import User
from polls.models import Poll, Answer

class PollForm(forms.ModelForm):     
    
    class Meta:
        model = Poll
        exclude = ('author','sites')
        