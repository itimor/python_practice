# -*- coding: utf-8 -*-
# Author: itimor
# Description: cmd input to web

from subprocess import check_output
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
import json
import sys
from .models import Record


def _record(record_list):
    '''save action record to db'''

    record = Record(user=record_list['user'],
                    brand=record_list['brand'],
                    from_ip=record_list['from_ip'],
                    cmd=record_list['cmd'],
                    action=record_list['action'])
    record.save()


def record(request):
    '''view action record to db'''

    record_fileds = Record._meta.get_fields()
    banned_fields = ['ID', u'命令', u'动作']
    filter_fields = {f.verbose_name: f.name for f in record_fileds
                     if f.verbose_name not in banned_fields}
    filter_str = str(datetime.now()).split()[0]
    filter_field = 'action_time'
    if request.POST.get('filter_str') and request.POST.get('filter_field'):
        filter_str = request.POST.get('filter_str')
        filter_field = filter_fields[request.POST.get('filter_field')]
    filter_field_contains = '%s__contains' % filter_field
    my_filter = {}
    my_filter[filter_field_contains] = filter_str
    records = Record.objects.filter(**my_filter) \
        .order_by('-action_time', 'user').values()

    context = {
        'records': records,
        'filter_fields': filter_fields
    }
    return render(request, "record.html", context)


def _action(cmd):
    '''
    execute cmd
    '''
    result = {}
    try:
        stdout = check_output(cmd)
        stderr = ''
    except:
        stdout = ''
        stderr = str(sys.exc_info())
    result['stdout'] = stdout
    result['stderr'] = stderr
    return result


def action(request):
    if request.method == 'POST' and request.is_ajax():
        result = request.POST

        # cmd = ['ping', '-c', '1', 'www.baidu.com']  # 测试命令，你可以定义的更复杂
        cmd = result['btncmd'].split()
        cmd_exec = _action(cmd)  # 调用执行函数，获得结果
        stdout = cmd_exec['stdout']
        stderr = cmd_exec['stderr']
        if not stdout:
            stdout = stderr
            # 保存操作记录
            # else:
            #    try:
            #        record_list = {
            #            'user': result['user'],
            #            'brand': result['selbrand',
            #            'from_ip': user_ip(request),
            #            'cmd': ' '.join(cmd),
            #            'action': 'TR',
            #        }
            #    except:
            #        print sys.exc_info()[0]
            #    _record(record_list)

        try:
            stdout = str(stdout)
            stdout = stdout.splitlines()
        except:
            e = sys.exc_info()[0]
            print "error" + str(e)

        return HttpResponse(json.dumps(stdout),
                            content_type="application/json")
    return HttpResponseNotFound('<h1>Page not found</h1>')


def demo(request):
    return render(request, "demo.html")