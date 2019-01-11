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

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif', 'bmp'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './tmp/'

data = { 'img': '/uploads/data/test1.jpg', 'msg' : 'your debug message'}

def makedirs(path):
    dir,fname = os.path.split(path)
    if not os.path.exists(dir):
        try:
            os.makedirs(dir)
        except:
            pass
            
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/uploads/<dir>/<filename>')
def uploaded_file(dir, filename):
    #dir,fname = os.path.split(path)
    #app.logger.error(path)
    return send_from_directory('./tmp/'+dir,filename)

@app.route('/post', methods=['GET', 'POST'])
def request_api():
    return request_handler(request, render_json)
    
@app.route('/ajax', methods=['GET', 'POST'])
def request_get():
    jstr = json.dumps(data)
    print(jstr)
    return jstr
    
def render_json(jdata, image_url, proc_time):
    return json.dumps(jdata)
    
def request_handler(request, render):
    if request.method == 'POST':
        file = request.files['file']
        msg = request.form.get("json",type=str,default='')
        if file and allowed_file(file.filename):
            date = datetime.datetime.now().strftime("%Y%m%d")
            stamp = datetime.datetime.now().strftime("%H-%M-%S-%f")
            ext = file.filename.rsplit('.', 1)[1]
            name = date + '/' + stamp + '.' + ext
            subdir, subname = os.path.split(name)
            #name = secure_filename(file.filename)
            path = os.path.join(app.config['UPLOAD_FOLDER'], name)
            makedirs(path)
            file.save(path)
            file_url = url_for('uploaded_file', dir=subdir, filename=subname)
            # update
            data['img'] = file_url            
            data['msg'] = msg
            return json.dumps(data)
            
    return render_template("index.html")

    
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template("index.html", freq=1000, showText='true')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
