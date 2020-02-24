#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 01:12:44 2020

@author: AkashTyagi
"""
import subprocess
from flask import request,Flask,render_template,jsonify
app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('terminal.html')


#@app.route('/terminal',methods=['POST'])
#def image_extracted():
#    command = request.form['command']
##    output = os.system(command)
#    return render_template('result.html',command=command)


@app.route('/terminal')
def background_process():
    command = request.args.get('proglang')
    proc = subprocess.Popen(command.split(), stdout=subprocess.PIPE, shell=False)
    (out, err) = proc.communicate()
    if err is None:
        output = str(out)[:-1].split("\\n")
    else:
        output = str(err)
    return jsonify(result=output)

if __name__ == '__main__':
    app.run(debug = True)
    app.run(port=5000)
#host='192.168.1.10'


