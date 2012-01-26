# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *


urlpatterns = patterns('polls.views',
    url(r'^poll/create/$',
        'poll_create',
        name='polls_poll_create'
    ),
    url(r'^poll/detail/(?P<poll_id>\d+)/$',
        'poll_detail',
        name='polls_poll_detail'
    ),
    url(r'^poll/list/',
        'poll_list',
        name='polls_poll_list'
    ),

)