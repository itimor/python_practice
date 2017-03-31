# -*- coding: utf-8 -*-
# Author: itimor
# Description: cmd input to web

from subprocess import check_output
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
import json
import sys

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
        print cmd
        cmd_exec = _action(cmd)  # 调用执行函数，获得结果
        stdout = cmd_exec['stdout']
        stderr = cmd_exec['stderr']
        if not stdout:
            stdout = stderr
        # else:
        #     try:
        #         record_list = {
        #             'user': request.POST['user'],
        #             'brand': selbrand,
        #             'from_ip': user_ip(request),
        #             'cmd': ' '.join(cmd),
        #             'action': 'TR',
        #         }
        #     except:
        #         print sys.exc_info()[0]
        #     _record(record_list)

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