from config import db_config
import pymysql
import json
from json_datetime import CJsonEncoder
from flask import render_template, redirect, Blueprint
from flask_login import login_required

slaRoute = Blueprint(
    'sla',
    __name__,
    url_prefix='/sla',
    template_folder='templates',
    static_folder='static'
)

@slaRoute.route('/')
@login_required
def index():
    return redirect('/sla/mengdian')

@slaRoute.route('/<page>')
@login_required
def page(page):
    conn = pymysql.connect(**db_config)
    cur = conn.cursor()
    sql = "SELECT * FROM %s_sla" % page
    data = cur.execute(sql)
    result = cur.fetchall()
    cur = conn.close()
    sladata = json.dumps(result, cls=CJsonEncoder)
    return render_template('sla.html', page=page, jsondata=sladata)