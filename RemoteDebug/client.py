# -*- coding: utf-8 -*-
import os
import sys
import json
import time
from requests_toolbelt import MultipartEncoder
import requests
import datetime

def post_request(server_url):
    filename = './tmp/data/test2.jpg'
    stamp = datetime.datetime.now().strftime("%Y%m%d-%H:%M:%S:%f")
    msg = stamp
    m = MultipartEncoder(
    fields={'json': msg,
            'file': ('image.jpg', open(filename, 'rb'), 'application/octet-stream')}
    )

    r = requests.post(server_url, data=m,
                  headers={'Content-Type': m.content_type})

    message = r.text
    return message
    
    
def main(server_url): 
    count = 0
    while True:
        beg = time.time()   
        message = post_request(server_url)
        end = time.time()
        jdata = json.loads(message)
        delay = (end - beg) * 1000
        count += 1
        #print(message)
        print("count:%-4d delay:%5.0f  reqlen:%d " % (count, delay, len(message)))
        time.sleep(5)

if __name__ == '__main__':     
    main('http://localhost:80/post')        