from __future__ import division
import datetime
from elasticsearch import Elasticsearch
import json
import pymysql

es = Elasticsearch("118.178.32.176:19200")
dt = (datetime.datetime.now() - datetime.timedelta(days = 1)).strftime("%Y.%m.%d")

db_config = {
          'host':'115.159.19.87',
          'port':3306,
          'user':'root',
          'password':'weimob@123',
          'db':'count_sla',
          'charset':'utf8mb4',
          'cursorclass':pymysql.cursors.DictCursor,
          }
conn = pymysql.connect(**db_config)
cur = conn.cursor()

config = {
    'index_name':'logstash-'+dt,
    'server':{'node':'m.vd.cn',
               'api':'api.vd.cn',
               'mapi':'mapi.vd.cn',
               'yunying':'10.252.218.121'},
}

with open('vd-txx.json', 'r') as f:
    data_txx = json.load(f)

with open('vd-4xx.json', 'r') as f:
    data_4xx = json.load(f)

with open('vd-5xx.json', 'r') as f:
    data_5xx = json.load(f)

with open('vd-2xx.json', 'r') as f:
    data_2xx = json.load(f)

with open('vd-404.json', 'r') as f:
    data_404 = json.load(f)

with open('vd-499.json', 'r') as f:
    data_499 = json.load(f)

for name,server in config['server'].items():
    data_2xx['query']['filtered']['filter']['bool']['must']['bool']['must'][0]['query']['match']['server']['query'] = server
    data_4xx['query']['filtered']['filter']['bool']['must']['bool']['must'][0]['query']['match']['server']['query'] = server
    data_5xx['query']['filtered']['filter']['bool']['must']['bool']['must'][0]['query']['match']['server']['query'] = server
    data_404['query']['filtered']['filter']['bool']['must']['bool']['must'][0]['query']['match']['server']['query'] = server
    data_499['query']['filtered']['filter']['bool']['must']['bool']['must'][0]['query']['match']['server']['query'] = server
    data_txx['query']['filtered']['filter']['bool']['must']['query']['match']['server']['query'] = server

    res_2xx = es.search(index=config['index_name'], body=data_2xx)
    res_4xx = es.search(index=config['index_name'], body=data_4xx)
    res_5xx = es.search(index=config['index_name'], body=data_5xx)
    res_txx = es.search(index=config['index_name'], body=data_txx)
    res_404 = es.search(index=config['index_name'], body=data_404)
    res_499 = es.search(index=config['index_name'], body=data_499)

    lst = [name,res_2xx['aggregations']['COUNT(*)']['value'],res_4xx['aggregations']['COUNT(*)']['value'],res_5xx['aggregations']['COUNT(*)']['value'],res_txx['aggregations']['COUNT(*)']['value'],res_404['aggregations']['COUNT(*)']['value'],res_499['aggregations']['COUNT(*)']['value']]
    success_percent = '%.4f%%'% float(lst[1]/lst[4]*100)
    four_percent = '%.4f%%'% float(lst[2]/lst[4]*100)
    five_percent = '%.4f%%' % float(lst[3] / lst[4]*100)

    sql = "insert into mengdian_sla values ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s',CURDATE())" % ('',lst[0],lst[4],lst[1],success_percent,lst[3],five_percent,lst[2],four_percent,lst[6],lst[5])
    print sql
    insert = cur.execute(sql)

conn.commit()
conn.close()




