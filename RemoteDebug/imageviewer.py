# -*- coding: utf-8 -*-
import os
import sys
from flask import Flask, request, url_for, send_from_directory, render_template
from werkzeug import secure_filename
import time
import json
import base64
import time
import uuid
import datetime
import random

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif', 'bmp'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './tmp/'

FREQ = 1000
img_path_file = 'filelist-rel.txt'
img_list = []
with open(img_path_file, 'r') as f:
    for line in f.readlines():
        line = line.strip()
        img_list.append('/static/' + line)
        
data = {'img': '/static/test1.jpg'}

def makedirs(path):
    dir,fname = os.path.split(path)
    if not os.path.exists(dir):
        try:
            os.makedirs(dir)
        except:
            pass
            
    
@app.route('/ajax', methods=['GET', 'POST'])
def request_get():
    # select random
    img = random.choice(img_list)
    data['img'] = img
    jstr = json.dumps(data)
    print(jstr)
    return jstr

    
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template("index.html", freq=FREQ, showText='false')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
