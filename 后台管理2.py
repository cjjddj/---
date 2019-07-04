# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 18:18:04 2019

@author: dell
"""

from flask import Flask,render_template,request
app=Flask(__name__)
from redis import StrictRedis
r=StrictRedis(decode_responses=True)

@app.route('/layui')
def layui():
    return render_template('layui.html') 
@app.route('/dataList3')
def dataList3():
    try:
        page=int(request.args.get('page'))
        rows=int(request.args.get('limit'))
        ls=r.lrange('urls2',(page-1)*rows,page*rows-1)
        values=r.hmget('qcwy_msg',ls)
        jsonstr1=','.join(values)
        jsonstr2='[{}]'.format(jsonstr1)
        j='{"code":0,"msg":"","count":'+str(r.llen('urls2'))+',"data":'+jsonstr2+'}'
        return j
    except Exception as err:
        return '参数错误'
app.run(host='192.168.2.119',port=5000)