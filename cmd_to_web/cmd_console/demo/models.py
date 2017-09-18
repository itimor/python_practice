# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class Record(models.Model):
    action_list = {
        ('TR', ('df', 'mkdir', 'free')),
    }
    user = models.CharField(max_length=20, verbose_name="用户")
    brand = models.CharField(max_length=20, verbose_name="品牌")
    from_ip = models.GenericIPAddressField(verbose_name="IP")
    cmd = models.CharField(max_length=50, verbose_name="命令")
    action = models.CharField(max_length=5, choices=action_list, verbose_name="动作")
    action_time = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="执行时间")