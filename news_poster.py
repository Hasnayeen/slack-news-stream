# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 15:53:41 2016

@author: hasnayeen
"""

import requests
import time
import json
from env import settings

def get_news():
    filename = time.strftime("%d-%m-%Y") + ".txt"
    with open(filename, 'r+') as f:
        line_list = f.readlines()
        for line_number in xrange(0, len(line_list)):
            flag = line_list[line_number].split("\t")[2].strip()
            if flag == "false":
                post_to_slack(line_list[line_number])
                line_list[line_number] = line_list[line_number].replace('false','true')
        
        f.seek(0)
        for line in line_list:
            f.write(line)
            
        f.truncate()
        
def post_to_slack(line):
    url = settings['url']
    title = line.split("\t")[0]
    link = line.split("\t")[1]
    message = "<" + link + "|" + title + ">"
    payload = json.dumps({'text':message})
    requests.post(url, data=payload)

get_news()