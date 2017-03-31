# -*- coding: utf-8 -*-
# Author: itimor
# Description: cmd input to web

from __future__ import unicode_literals
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^action/$', views.action, name='action'),
    url(r'^$', views.demo, name='demo'),
]
