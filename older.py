#coding = utf-8
#running in python3.6

import requests
import base64
from multiprocessing import Process
url_test = 'http://xxxxxxx'#接口

black_w = [

]
black_m = [
    
]

white_w =[
   
]
white_m = [
   
]

yellow_w = [
    
yellow_m = [
   
]

bw = [

]
bm = [

]

ww = [

]
wm = [

]

yw = [
"
]
ym = [

]


def bmm():
    count = 0
    for i in black_m:
        for j in bm:
            params_up = {
                "merge_url":"%s"%j,
                "template_rectangle":"",
                "template_url":"%s"%i,
                "merge_rectangle":"",
                "merge_rate":30
                }
            print(params_up)
            r = requests.post(url_test, json=params_up)
            strs = r.text
            try:
                imgadata = base64.b64decode(strs)
                count = count+1
                file = open('black_man_30_NO%s.jpg'%count, 'wb')
                file.write(imgadata)
                file.close()
            except:
                pass

    for i in black_m:
        for j in bm:
            params_up = {
                "merge_url":"%s"%j,
                "template_rectangle":"",
                "template_url":"%s"%i,
                "merge_rectangle":"",
                "merge_rate":40
                }
            print(params_up)
            r = requests.post(url_test, json=params_up)
            strs = r.text
            try:
                imgadata = base64.b64decode(strs)
                count = count+1
                file = open('black_man_40_NO%s.jpg'%count, 'wb')
                file.write(imgadata)
                file.close()
            except:
                pass

    for i in black_m:
        for j in bm:
            params_up = {
                "merge_url":"%s"%j,
                "template_rectangle":"",
                "template_url":"%s"%i,
                "merge_rectangle":"",
                "merge_rate":50
                }
            print(params_up)
            r = requests.post(url_test, json=params_up)
            strs = r.text
            try:
                imgadata = base64.b64decode(strs)
                count = count+1
                file = open('black_man_50_NO%s.jpg'%count, 'wb')
                file.write(imgadata)
                file.close()
            except:
                pass

    for i in black_m:
        for j in bm:
            params_up = {
                "merge_url":"%s"%j,
                "template_rectangle":"",
                "template_url":"%s"%i,
                "merge_rectangle":"",
                "merge_rate":60
                }
            print(params_up)
            r = requests.post(url_test, json=params_up)
            strs = r.text
            try:
                imgadata = base64.b64decode(strs)
                count = count+1
                file = open('black_man_60_NO%s.jpg'%count, 'wb')
                file.write(imgadata)
                file.close()
            except:
                pass

    for i in black_m:
        for j in bm:
            params_up = {
                "merge_url":"%s"%j,
                "template_rectangle":"",
                "template_url":"%s"%i,
                "merge_rectangle":"",
                "merge_rate":70
                }
            print(params_up)
            r = requests.post(url_test, json=params_up)
            strs = r.text
            try:
                imgadata = base64.b64decode(strs)
                count = count+1
                file = open('black_man_70_NO%s.jpg'%count, 'wb')
                file.write(imgadata)
                file.close()
            except:
                pass

    for i in black_m:
        for j in bm:
            params_up = {
                "merge_url":"%s"%j,
                "template_rectangle":"",
                "template_url":"%s"%i,
                "merge_rectangle":"",
                "merge_rate":80
                }
            print(params_up)
            r = requests.post(url_test, json=params_up)
            strs = r.text
            try:
                imgadata = base64.b64decode(strs)
                count = count+1
                file = open('black_man_80_NO%s.jpg'%count, 'wb')
                file.write(imgadata)
                file.close()
            except:
                pass

    for i in black_m:
        for j in bm:
            params_up = {
                "merge_url":"%s"%j,
                "template_rectangle":"",
                "template_url":"%s"%i,
                "merge_rectangle":"",
                "merge_rate":90
                }
            print(params_up)
            r = requests.post(url_test, json=params_up)
            strs = r.text
            try:
                imgadata = base64.b64decode(strs)
                count = count+1
                file = open('black_man_90_NO%s.jpg'%count, 'wb')
                file.write(imgadata)
                file.close()
            except:
                pass

def bww():
    count = 0
    for i in black_w:
        for j in bw:
            params_up = {
                "merge_url":"%s"%j,
                "template_rectangle":"",
                "template_url":"%s"%i,
                "merge_rectangle":"",
                "merge_rate":30
                }
            print(params_up)
            r = requests.post(url_test, json=params_up)
            strs = r.text
            try:
                imgadata = base64.b64decode(strs)
                count = count+1
                file = open('black_woman_30_NO%s.jpg'%count, 'wb')
                file.write(imgadata)
                file.close()
            except:
                pass

    for i in black_w:
        for j in bw:
            params_up = {
                "merge_url":"%s"%j,
                "template_rectangle":"",
                "template_url":"%s"%i,
                "merge_rectangle":"",
                "merge_rate":40
                }
            print(params_up)
            r = requests.post(url_test, json=params_up)
            strs = r.text
            try:
                imgadata = base64.b64decode(strs)
                count = count+1
                file = open('black_woman_40_NO%s.jpg'%count, 'wb')
                file.write(imgadata)
                file.close()
            except:
                pass

    for i in black_w:
        for j in bw:
            params_up = {
                "merge_url":"%s"%j,
                "template_rectangle":"",
                "template_url":"%s"%i,
                "merge_rectangle":"",
                "merge_rate":50
                }
            print(params_up)
            r = requests.post(url_test, json=params_up)
            strs = r.text
            try:
                imgadata = base64.b64decode(strs)
                count = count+1
                file = open('black_woman_50_NO%s.jpg'%count, 'wb')
                file.write(imgadata)
                file.close()
            except:
                pass

    for i in black_w:
        for j in bw:
            params_up = {
                "merge_url":"%s"%j,
                "template_rectangle":"",
                "template_url":"%s"%i,
                "merge_rectangle":"",
                "merge_rate":60
                }
            print(params_up)
            r = requests.post(url_test, json=params_up)
            strs = r.text
            try:
                imgadata = base64.b64decode(strs)
                count = count+1
                file = open('black_woman_60_NO%s.jpg'%count, 'wb')
                file.write(imgadata)
                file.close()
            except:
                pass

    for i in black_w:
        for j in bw:
            params_up = {
                "merge_url":"%s"%j,
                "template_rectangle":"",
                "template_url":"%s"%i,
                "merge_rectangle":"",
                "merge_rate":70
                }
            print(params_up)
            r = requests.post(url_test, json=params_up)
            strs = r.text
            try:
                imgadata = base64.b64decode(strs)
                count = count+1
                file = open('black_woman_70_NO%s.jpg'%count, 'wb')
                file.write(imgadata)
                file.close()
            except:
                pass

    for i in black_w:
        for j in bw:
            params_up = {
                "merge_url":"%s"%j,
                "template_rectangle":"",
                "template_url":"%s"%i,
                "merge_rectangle":"",
                "merge_rate":80
                }
            print(params_up)
            r = requests.post(url_test, json=params_up)
            strs = r.text
            try:
                imgadata = base64.b64decode(strs)
                count = count+1
                file = open('black_woman_80_NO%s.jpg'%count, 'wb')
                file.write(imgadata)
                file.close()
            except:
                pass

    for i in black_w:
        for j in bw:
            params_up = {
                "merge_url":"%s"%j,
                "template_rectangle":"",
                "template_url":"%s"%i,
                "merge_rectangle":"",
                "merge_rate":90
                }
            print(params_up)
            r = requests.post(url_test, json=params_up)
            strs = r.text
            try:
                imgadata = base64.b64decode(strs)
                count = count+1
                file = open('black_woman_90_NO%s.jpg'%count, 'wb')
                file.write(imgadata)
                file.close()
            except:
                pass

def www():
    count = 0
    for i in white_w:
        for j in ww:
            params_up = {
                "merge_url":"%s"%j,
                "template_rectangle":"",
                "template_url":"%s"%i,
                "merge_rectangle":"",
                "merge_rate":30
                }
            print(params_up)
            r = requests.post(url_test, json=params_up)
            strs = r.text
            try:
                imgadata = base64.b64decode(strs)
                count = count+1
                file = open('white_woman_30_NO%s.jpg'%count, 'wb')
                file.write(imgadata)
                file.close()
            except:
                pass

    for i in white_w:
        for j in ww:
            params_up = {
                "merge_url":"%s"%j,
                "template_rectangle":"",
                "template_url":"%s"%i,
                "merge_rectangle":"",
                "merge_rate":40
                }
            print(params_up)
            r = requests.post(url_test, json=params_up)
            strs = r.text
            try:
                imgadata = base64.b64decode(strs)
                count = count+1
                file = open('white_woman_40_NO%s.jpg'%count, 'wb')
                file.write(imgadata)
                file.close()
            except:
                pass

    for i in white_w:
        for j in ww:
            params_up = {
                "merge_url":"%s"%j,
                "template_rectangle":"",
                "template_url":"%s"%i,
                "merge_rectangle":"",
                "merge_rate":50
                }
            print(params_up)
            r = requests.post(url_test, json=params_up)
            strs = r.text
            try:
                imgadata = base64.b64decode(strs)
                count = count+1
                file = open('white_woman_50_NO%s.jpg'%count, 'wb')
                file.write(imgadata)
                file.close()
            except:
                pass

    for i in white_w:
        for j in ww:
            params_up = {
                "merge_url":"%s"%j,
                "template_rectangle":"",
                "template_url":"%s"%i,
                "merge_rectangle":"",
                "merge_rate":60
                }
            print(params_up)
            r = requests.post(url_test, json=params_up)
            strs = r.text
            try:
                imgadata = base64.b64decode(strs)
                count = count+1
                file = open('white_woman_60_NO%s.jpg'%count, 'wb')
                file.write(imgadata)
                file.close()
            except:
                pass

    for i in white_w:
        for j in ww:
            params_up = {
                "merge_url":"%s"%j,
                "template_rectangle":"",
                "template_url":"%s"%i,
                "merge_rectangle":"",
                "merge_rate":70
                }
            print(params_up)
            r = requests.post(url_test, json=params_up)
            strs = r.text
            try:
                imgadata = base64.b64decode(strs)
                count = count+1
                file = open('white_woman_70_NO%s.jpg'%count, 'wb')
                file.write(imgadata)
                file.close()
            except:
                pass

    for i in white_w:
        for j in ww:
            params_up = {
                "merge_url":"%s"%j,
                "template_rectangle":"",
                "template_url":"%s"%i,
                "merge_rectangle":"",
                "merge_rate":80
                }
            print(params_up)
            r = requests.post(url_test, json=params_up)
            strs = r.text
            try:
                imgadata = base64.b64decode(strs)
                count = count+1
                file = open('white_woman_80_NO%s.jpg'%count, 'wb')
                file.write(imgadata)
                file.close()
            except:
                pass

    for i in white_w:
        for j in ww:
            params_up = {
                "merge_url":"%s"%j,
                "template_rectangle":"",
                "template_url":"%s"%i,
                "merge_rectangle":"",
                "merge_rate":90
                }
            print(params_up)
            r = requests.post(url_test, json=params_up)
            strs = r.text
            try:
                imgadata = base64.b64decode(strs)
                count = count+1
                file = open('white_woman_90_NO%s.jpg'%count, 'wb')
                file.write(imgadata)
                file.close()
            except:
                pass

def wmm():
    count = 0
    for i in white_m:
        for j in wm:
            params_up = {
                "merge_url":"%s"%j,
                "template_rectangle":"",
                "template_url":"%s"%i,
                "merge_rectangle":"",
                "merge_rate":30
                }
            print(params_up)
            r = requests.post(url_test, json=params_up)
            strs = r.text
            try:
                imgadata = base64.b64decode(strs)
                count = count+1
                file = open('white_man_30_NO%s.jpg'%count, 'wb')
                file.write(imgadata)
                file.close()
            except:
                pass

    for i in white_m:
        for j in wm:
            params_up = {
                "merge_url":"%s"%j,
                "template_rectangle":"",
                "template_url":"%s"%i,
                "merge_rectangle":"",
                "merge_rate":40
                }
            print(params_up)
            r = requests.post(url_test, json=params_up)
            strs = r.text
            try:
                imgadata = base64.b64decode(strs)
                count = count+1
                file = open('white_man_40_NO%s.jpg'%count, 'wb')
                file.write(imgadata)
                file.close()
            except:
                pass

    for i in white_m:
        for j in wm:
            params_up = {
                "merge_url":"%s"%j,
                "template_rectangle":"",
                "template_url":"%s"%i,
                "merge_rectangle":"",
                "merge_rate":50
                }
            print(params_up)
            r = requests.post(url_test, json=params_up)
            strs = r.text
            try:
                imgadata = base64.b64decode(strs)
                count = count+1
                file = open('white_man_50_NO%s.jpg'%count, 'wb')
                file.write(imgadata)
                file.close()
            except:
                pass

    for i in white_m:
        for j in wm:
            params_up = {
                "merge_url":"%s"%j,
                "template_rectangle":"",
                "template_url":"%s"%i,
                "merge_rectangle":"",
                "merge_rate":60
                }
            print(params_up)
            r = requests.post(url_test, json=params_up)
            strs = r.text
            try:
                imgadata = base64.b64decode(strs)
                count = count+1
                file = open('white_man_60_NO%s.jpg'%count, 'wb')
                file.write(imgadata)
                file.close()
            except:
                pass

    for i in white_m:
        for j in wm:
            params_up = {
                "merge_url":"%s"%j,
                "template_rectangle":"",
                "template_url":"%s"%i,
                "merge_rectangle":"",
                "merge_rate":70
                }
            print(params_up)
            r = requests.post(url_test, json=params_up)
            strs = r.text
            try:
                imgadata = base64.b64decode(strs)
                count = count+1
                file = open('white_man_70_NO%s.jpg'%count, 'wb')
                file.write(imgadata)
                file.close()
            except:
                pass

    for i in white_m:
        for j in wm:
            params_up = {
                "merge_url":"%s"%j,
                "template_rectangle":"",
                "template_url":"%s"%i,
                "merge_rectangle":"",
                "merge_rate":80
                }
            print(params_up)
            r = requests.post(url_test, json=params_up)
            strs = r.text
            try:
                imgadata = base64.b64decode(strs)
                count = count+1
                file = open('white_man_80_NO%s.jpg'%count, 'wb')
                file.write(imgadata)
                file.close()
            except:
                pass

    for i in white_m:
        for j in wm:
            params_up = {
                "merge_url":"%s"%j,
                "template_rectangle":"",
                "template_url":"%s"%i,
                "merge_rectangle":"",
                "merge_rate":90
                }
            print(params_up)
            r = requests.post(url_test, json=params_up)
            strs = r.text
            try:
                imgadata = base64.b64decode(strs)
                count = count+1
                file = open('white_man_90_NO%s.jpg'%count, 'wb')
                file.write(imgadata)
                file.close()
            except:
                pass

def ymm():
    count = 0
    for i in yellow_m:
        for j in ym:
            params_up = {
                "merge_url":"%s"%j,
                "template_rectangle":"",
                "template_url":"%s"%i,
                "merge_rectangle":"",
                "merge_rate":30
                }
            print(params_up)
            r = requests.post(url_test, json=params_up)
            strs = r.text
            try:
                imgadata = base64.b64decode(strs)
                count = count+1
                file = open('yellow_man_30_NO%s.jpg'%count, 'wb')
                file.write(imgadata)
                file.close()
            except:
                pass

    for i in yellow_m:
        for j in ym:
            params_up = {
                "merge_url":"%s"%j,
                "template_rectangle":"",
                "template_url":"%s"%i,
                "merge_rectangle":"",
                "merge_rate":40
                }
            print(params_up)
            r = requests.post(url_test, json=params_up)
            strs = r.text
            try:
                imgadata = base64.b64decode(strs)
                count = count+1
                file = open('yellow_man_40_NO%s.jpg'%count, 'wb')
                file.write(imgadata)
                file.close()
            except:
                pass

    for i in yellow_m:
        for j in ym:
            params_up = {
                "merge_url":"%s"%j,
                "template_rectangle":"",
                "template_url":"%s"%i,
                "merge_rectangle":"",
                "merge_rate":50
                }
            print(params_up)
            r = requests.post(url_test, json=params_up)
            strs = r.text
            try:
                imgadata = base64.b64decode(strs)
                count = count+1
                file = open('yellow_man_50_NO%s.jpg'%count, 'wb')
                file.write(imgadata)
                file.close()
            except:
                pass

    for i in yellow_m:
        for j in ym:
            params_up = {
                "merge_url":"%s"%j,
                "template_rectangle":"",
                "template_url":"%s"%i,
                "merge_rectangle":"",
                "merge_rate":60
                }
            print(params_up)
            r = requests.post(url_test, json=params_up)
            strs = r.text
            try:
                imgadata = base64.b64decode(strs)
                count = count+1
                file = open('yellow_man_60_NO%s.jpg'%count, 'wb')
                file.write(imgadata)
                file.close()
            except:
                pass

    for i in yellow_m:
        for j in ym:
            params_up = {
                "merge_url":"%s"%j,
                "template_rectangle":"",
                "template_url":"%s"%i,
                "merge_rectangle":"",
                "merge_rate":70
                }
            print(params_up)
            r = requests.post(url_test, json=params_up)
            strs = r.text
            try:
                imgadata = base64.b64decode(strs)
                count = count+1
                file = open('yellow_man_70_NO%s.jpg'%count, 'wb')
                file.write(imgadata)
                file.close()
            except:
                pass

    for i in yellow_m:
        for j in ym:
            params_up = {
                "merge_url":"%s"%j,
                "template_rectangle":"",
                "template_url":"%s"%i,
                "merge_rectangle":"",
                "merge_rate":80
                }
            print(params_up)
            r = requests.post(url_test, json=params_up)
            strs = r.text
            try:
                imgadata = base64.b64decode(strs)
                count = count+1
                file = open('yellow_man_80_NO%s.jpg'%count, 'wb')
                file.write(imgadata)
                file.close()
            except:
                pass

    for i in yellow_m:
        for j in ym:
            params_up = {
                "merge_url":"%s"%j,
                "template_rectangle":"",
                "template_url":"%s"%i,
                "merge_rectangle":"",
                "merge_rate":90
                }
            print(params_up)
            r = requests.post(url_test, json=params_up)
            strs = r.text
            try:
                imgadata = base64.b64decode(strs)
                count = count+1
                file = open('yellow_man_90_NO%s.jpg'%count, 'wb')
                file.write(imgadata)
                file.close()
            except:
                pass

def yww():
    count = 0
    for i in yellow_w:
        for j in yw:
            params_up = {
                "merge_url":"%s"%j,
                "template_rectangle":"",
                "template_url":"%s"%i,
                "merge_rectangle":"",
                "merge_rate":30
                }
            print(params_up)
            r = requests.post(url_test, json=params_up)
            strs = r.text
            try:
                imgadata = base64.b64decode(strs)
                count = count+1
                file = open('yellow_woman_30_NO%s.jpg'%count, 'wb')
                file.write(imgadata)
                file.close()
            except:
                pass

    for i in yellow_w:
        for j in yw:
            params_up = {
                "merge_url":"%s"%j,
                "template_rectangle":"",
                "template_url":"%s"%i,
                "merge_rectangle":"",
                "merge_rate":40
                }
            print(params_up)
            r = requests.post(url_test, json=params_up)
            strs = r.text
            try:
                imgadata = base64.b64decode(strs)
                count = count+1
                file = open('yellow_woman_40_NO%s.jpg'%count, 'wb')
                file.write(imgadata)
                file.close()
            except:
                pass

    for i in yellow_w:
        for j in yw:
            params_up = {
                "merge_url":"%s"%j,
                "template_rectangle":"",
                "template_url":"%s"%i,
                "merge_rectangle":"",
                "merge_rate":50
                }
            print(params_up)
            r = requests.post(url_test, json=params_up)
            strs = r.text
            try:
                imgadata = base64.b64decode(strs)
                count = count+1
                file = open('yellow_woman_50_NO%s.jpg'%count, 'wb')
                file.write(imgadata)
                file.close()
            except:
                pass

    for i in yellow_w:
        for j in yw:
            params_up = {
                "merge_url":"%s"%j,
                "template_rectangle":"",
                "template_url":"%s"%i,
                "merge_rectangle":"",
                "merge_rate":60
                }
            print(params_up)
            r = requests.post(url_test, json=params_up)
            strs = r.text
            try:
                imgadata = base64.b64decode(strs)
                count = count+1
                file = open('yellow_woman_60_NO%s.jpg'%count, 'wb')
                file.write(imgadata)
                file.close()
            except:
                pass

    for i in yellow_w:
        for j in yw:
            params_up = {
                "merge_url":"%s"%j,
                "template_rectangle":"",
                "template_url":"%s"%i,
                "merge_rectangle":"",
                "merge_rate":70
                }
            print(params_up)
            r = requests.post(url_test, json=params_up)
            strs = r.text
            try:
                imgadata = base64.b64decode(strs)
                count = count+1
                file = open('yellow_woman_70_NO%s.jpg'%count, 'wb')
                file.write(imgadata)
                file.close()
            except:
                pass

    for i in yellow_w:
        for j in yw:
            params_up = {
                "merge_url":"%s"%j,
                "template_rectangle":"",
                "template_url":"%s"%i,
                "merge_rectangle":"",
                "merge_rate":80
                }
            print(params_up)
            r = requests.post(url_test, json=params_up)
            strs = r.text
            try:
                imgadata = base64.b64decode(strs)
                count = count+1
                file = open('yellow_woman_80_NO%s.jpg'%count, 'wb')
                file.write(imgadata)
                file.close()
            except:
                pass

    for i in yellow_w:
        for j in yw:
            params_up = {
                "merge_url":"%s"%j,
                "template_rectangle":"",
                "template_url":"%s"%i,
                "merge_rectangle":"",
                "merge_rate":90
                }
            print(params_up)
            r = requests.post(url_test, json=params_up)
            strs = r.text
            try:
                imgadata = base64.b64decode(strs)
                count = count+1
                file = open('yellow_woman_90_NO%s.jpg'%count, 'wb')
                file.write(imgadata)
                file.close()
            except:
                pass

if __name__ == '__main__' :
    Process(target=bmm).start()
    Process(target=bww).start()
    Process(target=www).start()
    Process(target=wmm).start()
    Process(target=ymm).start()
    Process(target=yww).start()

#template_url 为模板
#merge_url 为自己

#print(r.text)







