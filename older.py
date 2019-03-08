#coding = utf-8
#running in python3.6

import requests
import base64
from multiprocessing import Process
url_test = 'http://vision.3g.net.cn/api/v1/research/face_swap'

black_w = [
    "http://resource.gomocdn.com/a11e-2019-01-31-18-37-00/soft/face/template/7hByimtF.jpg",
    "http://resource.gomocdn.com/b114-2019-01-31-18-37-49/soft/face/template/gTMfAe3d.jpg",
    "http://resource.gomocdn.com/9d7c-2019-01-31-19-05-30/soft/face/template/rcI0ava1.jpg",
    "http://resource.gomocdn.com/f6b5-2019-01-31-19-06-23/soft/face/template/huB1qp7D.jpg"
]
black_m = [
    "http://resource.gomocdn.com/be32-2019-01-31-19-15-11/soft/face/template/QgYiyW3R.jpg",
    "http://resource.gomocdn.com/b610-2019-01-31-19-15-34/soft/face/template/kMeokSYz.jpg",
    "http://resource.gomocdn.com/2f39-2019-01-31-19-15-48/soft/face/template/47mlzLLq.jpg",
    "http://resource.gomocdn.com/fe9b-2019-01-31-19-15-59/soft/face/template/FFWifGoq.jpg",
    "http://resource.gomocdn.com/803b-2019-01-31-19-16-21/soft/face/template/cUBevRP1.jpg"
]

white_w =[
    "http://resource.gomocdn.com/eb27-2019-01-31-19-07-47/soft/face/template/4dSP2mUe.jpg",
    "http://resource.gomocdn.com/2753-2019-01-31-19-08-02/soft/face/template/ceY2jLLS.jpg",
    "http://resource.gomocdn.com/cfbb-2019-01-31-19-08-14/soft/face/template/TCk0B5D2.jpg",
    "http://resource.gomocdn.com/10da-2019-01-31-19-08-26/soft/face/template/QGoSkkJR.jpg"
]
white_m = [
    "http://resource.gomocdn.com/43d7-2019-01-31-19-18-33/soft/face/template/8GeD29tE.jpg",
    "http://resource.gomocdn.com/037c-2019-01-31-19-18-49/soft/face/template/APHPYXZB.jpg",
    "http://resource.gomocdn.com/2d6c-2019-01-31-19-19-02/soft/face/template/nmtHwxyh.jpg",
    "http://resource.gomocdn.com/100e-2019-01-31-19-19-13/soft/face/template/n9rXIQ9Y.jpg"
]

yellow_w = [
    "http://resource.gomocdn.com/6537-2019-01-31-19-09-48/soft/face/template/g2T2clw8.jpg",
    "http://resource.gomocdn.com/3b88-2019-01-31-19-10-05/soft/face/template/p8tFEHvn.jpg",
    "http://resource.gomocdn.com/a3bc-2019-01-31-19-10-19/soft/face/template/14PnvrPG.jpg",
    "http://resource.gomocdn.com/a200-2019-01-31-19-10-31/soft/face/template/DFARWOCJ.jpg"
]
yellow_m = [
    "http://resource.gomocdn.com/b3d2-2019-01-31-19-11-45/soft/face/template/CR5N1LRz.jpg",
    "http://resource.gomocdn.com/25ee-2019-01-31-19-12-00/soft/face/template/YqEI3mqJ.jpg",
    "http://resource.gomocdn.com/23e9-2019-01-31-19-12-16/soft/face/template/FlbUN1Sq.jpg",
    "http://resource.gomocdn.com/a509-2019-01-31-19-12-29/soft/face/template/RPYoCInV.jpg"
]

bw = [
    "http://resource.gomocdn.com/789b-2019-01-15-19-45-33/soft/face/template/VdpSX5uK.jpg",
    "http://resource.gomocdn.com/9900-2019-01-18-17-09-18/soft/face/template/AMvjVjfb.jpg",
    "http://resource.gomocdn.com/5c5f-2019-01-18-17-09-51/soft/face/template/ePvpneVB.jpg",
    "http://resource.gomocdn.com/4a3d-2019-01-18-17-11-18/soft/face/template/HDSvGKI6.jpg",
    "http://resource.gomocdn.com/8f03-2019-01-18-17-12-13/soft/face/template/suLnLWjr.jpg",
    "http://resource.gomocdn.com/a316-2019-01-18-17-12-57/soft/face/template/ET7mBQVJ.jpg",
    "http://resource.gomocdn.com/dfd4-2019-01-23-17-47-24/soft/face/template/VGDEcDpN.jpg",
    "http://resource.gomocdn.com/c6bd-2019-01-23-17-48-26/soft/face/template/wO9rpVAx.jpg",
    "http://resource.gomocdn.com/a2db-2019-01-23-17-49-14/soft/face/template/OQEduugy.jpg",
    "http://resource.gomocdn.com/6ed9-2019-01-23-17-49-56/soft/face/template/2eqtGTEe.jpg",
    "http://resource.gomocdn.com/a392-2019-01-23-17-50-41/soft/face/template/JLE9YOO8.jpg",
    "http://resource.gomocdn.com/1bbf-2019-01-23-17-51-29/soft/face/template/wUTqAyD0.jpg",
    "http://resource.gomocdn.com/5069-2019-01-23-17-52-22/soft/face/template/LhVlnbRm.jpg",
    "http://resource.gomocdn.com/4cd6-2019-01-23-17-54-06/soft/face/template/4r55U0Fs.jpg",
    "http://resource.gomocdn.com/3e54-2019-01-23-17-54-49/soft/face/template/LlwRxpBA.jpg",
    "http://resource.gomocdn.com/f9c4-2019-01-23-17-55-44/soft/face/template/o9bycPCk.jpg",
    "http://resource.gomocdn.com/7590-2019-01-23-17-56-21/soft/face/template/56ZK4Q9S.jpg"
]
bm = [
    "http://resource.gomocdn.com/2ee9-2019-01-15-19-45-09/soft/face/template/r3LBzIlt.jpg",
    "http://resource.gomocdn.com/9761-2019-01-18-17-06-49/soft/face/template/0dgjr6uh.jpg",
    "http://resource.gomocdn.com/410d-2019-01-18-17-07-27/soft/face/template/2cZ3OYed.jpg",
    "http://resource.gomocdn.com/a159-2019-01-18-17-08-03/soft/face/template/CCW2qRnx.jpg",
    "http://resource.gomocdn.com/ad2e-2019-01-18-17-08-35/soft/face/template/sx2rMdhx.jpg",
    "http://resource.gomocdn.com/23a4-2019-01-18-17-35-39/soft/face/template/4biA3jR3.jpg",
    "http://resource.gomocdn.com/b24d-2019-01-23-17-36-19/soft/face/template/3wDbxEZS.jpg",
    "http://resource.gomocdn.com/19c3-2019-01-23-17-37-11/soft/face/template/2Dmtc2JK.jpg",
    "http://resource.gomocdn.com/dad3-2019-01-23-17-39-08/soft/face/template/9ehy5jk0.jpg",
    "http://resource.gomocdn.com/f400-2019-01-23-17-40-02/soft/face/template/UvQ8lPMm.jpg",
    "http://resource.gomocdn.com/e9cc-2019-01-23-17-40-51/soft/face/template/GVY3uGig.jpg",
    "http://resource.gomocdn.com/4663-2019-01-23-17-42-19/soft/face/template/IsBhHkCw.jpg",
    "http://resource.gomocdn.com/87c4-2019-01-23-17-43-06/soft/face/template/LOJYrGzv.jpg",
    "http://resource.gomocdn.com/5354-2019-01-23-17-43-48/soft/face/template/uvqfvvK8.jpg",
    "http://resource.gomocdn.com/2ca6-2019-01-23-17-45-16/soft/face/template/J0HINi85.jpg",
    "http://resource.gomocdn.com/75d1-2019-01-23-17-46-04/soft/face/template/ZwnY4lhj.jpg",
    "http://resource.gomocdn.com/2e1e-2019-01-23-17-46-53/soft/face/template/bUEUIPEQ.jpg"
]

ww = [
    "http://resource.gomocdn.com/7016-2019-01-15-19-44-46/soft/face/template/crd9Kl8X.jpg",
    "http://resource.gomocdn.com/7679-2019-01-18-17-00-05/soft/face/template/cufOFiGS.jpg",
    "http://resource.gomocdn.com/a11e-2019-01-18-17-02-54/soft/face/template/Kz6OaquX.jpg",
    "http://resource.gomocdn.com/b636-2019-01-18-17-03-36/soft/face/template/0QE5t4hQ.jpg",
    "http://resource.gomocdn.com/a099-2019-01-18-17-04-03/soft/face/template/ynWF5422.jpg",
    "http://resource.gomocdn.com/e503-2019-01-18-17-04-37/soft/face/template/6ETqxRBZ.jpg",
    "http://resource.gomocdn.com/f1df-2019-01-18-17-05-09/soft/face/template/qhwuzvNn.jpg",
    "http://resource.gomocdn.com/fb45-2019-01-23-17-20-15/soft/face/template/OzlOcT06.jpg",
    "http://resource.gomocdn.com/581a-2019-01-23-17-21-28/soft/face/template/SYHZ9PFH.jpg",
    "http://resource.gomocdn.com/f9b6-2019-01-23-17-22-39/soft/face/template/MpkuzYIZ.jpg",
    "http://resource.gomocdn.com/8c89-2019-01-23-17-24-16/soft/face/template/yNYmBbSD.jpg",
    "http://resource.gomocdn.com/5c1a-2019-01-23-17-22-19/soft/face/template/EgLfHKZT.jpg",
    "http://resource.gomocdn.com/370e-2019-01-23-17-23-31/soft/face/template/YQTvbrxR.jpg",
    "http://resource.gomocdn.com/63c1-2019-01-23-17-25-07/soft/face/template/YwSG98Gl.jpg",
    "http://resource.gomocdn.com/3f3e-2019-01-23-16-56-38/soft/face/template/bBmV9obL.jpg",
    "http://resource.gomocdn.com/a5f8-2019-01-23-17-31-17/soft/face/template/ITglT6zu.jpg",
    "http://resource.gomocdn.com/a082-2019-01-23-17-31-56/soft/face/template/K2ltgIsb.jpg",
    "http://resource.gomocdn.com/17e9-2019-01-23-17-32-18/soft/face/template/5n0fr313.jpg",
    "http://resource.gomocdn.com/e013-2019-01-23-17-33-01/soft/face/template/8Y23Uw6i.jpg",
    "http://resource.gomocdn.com/551e-2019-01-23-17-33-52/soft/face/template/vOfDrmAo.jpg",
    "http://resource.gomocdn.com/3e31-2019-01-23-17-34-28/soft/face/template/8sOBXNsc.jpg",
    "http://resource.gomocdn.com/3f3e-2019-01-23-16-56-38/soft/face/template/bBmV9obL.jpg"
]
wm = [
    "http://resource.gomocdn.com/07fe-2019-01-15-19-44-27/soft/face/template/8TwqaHgD.jpg",
    "http://resource.gomocdn.com/ea33-2019-01-18-16-48-29/soft/face/template/TvwVaSWO.jpg",
    "http://resource.gomocdn.com/319c-2019-01-18-16-56-42/soft/face/template/sp8ndBOp.jpg",
    "http://resource.gomocdn.com/6e09-2019-01-18-16-57-36/soft/face/template/tsZ34ITq.jpg",
    "http://resource.gomocdn.com/237c-2019-01-18-16-58-14/soft/face/template/5brRdaXM.jpg",
    "http://resource.gomocdn.com/9fc3-2019-01-18-16-58-48/soft/face/template/haRQ8czy.jpg",
    "http://resource.gomocdn.com/f2a8-2019-01-18-17-36-39/soft/face/template/ikcD1ciu.jpg",
    "http://resource.gomocdn.com/4886-2019-01-23-16-59-07/soft/face/template/wN1pwhB6.jpg",
    "http://resource.gomocdn.com/c82c-2019-01-23-17-00-14/soft/face/template/eJ4FkVl8.jpg",
    "http://resource.gomocdn.com/ca13-2019-01-23-17-08-38/soft/face/template/o6f8kdX8.jpg",
    "http://resource.gomocdn.com/0973-2019-01-23-17-10-44/soft/face/template/sCmNXoKf.jpg",
    "http://resource.gomocdn.com/0e85-2019-01-23-17-11-31/soft/face/template/funqDXkM.jpg",
    "http://resource.gomocdn.com/7ae8-2019-01-23-17-12-49/soft/face/template/MyLr2u0X.jpg",
    "http://resource.gomocdn.com/37bf-2019-01-23-17-14-12/soft/face/template/WXoF7QNz.jpg",
    "http://resource.gomocdn.com/8e87-2019-01-23-17-15-23/soft/face/template/Dshmi9lc.jpg",
    "http://resource.gomocdn.com/7989-2019-01-23-17-16-14/soft/face/template/9ogUR0mH.jpg",
    "http://resource.gomocdn.com/4e17-2019-01-23-17-17-00/soft/face/template/yDKudf64.jpg",
    "http://resource.gomocdn.com/f341-2019-01-23-17-18-27/soft/face/template/5w7zxQxr.jpg",
    "http://resource.gomocdn.com/396a-2019-01-23-17-17-42/soft/face/template/5jE6fkbx.jpg",
    "http://resource.gomocdn.com/e165-2019-01-23-17-19-39/soft/face/template/VFpUVIZL.jpg",
    "http://resource.gomocdn.com/027a-2019-01-23-17-19-22/soft/face/template/QLuqm5ZN.jpg"
]

yw = [
    "http://resource.gomocdn.com/0ae8-2019-01-15-19-48-47/soft/face/template/JEwyOur6.jpg",
    "http://resource.gomocdn.com/cb12-2019-01-18-17-18-16/soft/face/template/q2e70ZiG.jpg",
    "http://resource.gomocdn.com/2413-2019-01-18-17-26-54/soft/face/template/ylhsWc8A.jpg",
    "http://resource.gomocdn.com/3d2e-2019-01-18-17-27-47/soft/face/template/xZUQECAm.jpg",
    "http://resource.gomocdn.com/ecf8-2019-01-18-17-28-13/soft/face/template/XvKhBrIp.jpg",
    "http://resource.gomocdn.com/836f-2019-01-18-17-28-45/soft/face/template/bk2U9GtV.jpg",
    "http://resource.gomocdn.com/32eb-2019-01-18-17-29-26/soft/face/template/wUN7wX0F.jpg",
    "http://resource.gomocdn.com/ee82-2019-01-24-10-39-26/soft/face/template/tNuujUNL.jpg",
    "http://resource.gomocdn.com/762b-2019-01-24-10-40-06/soft/face/template/Ao3BFKve.jpg",
    "http://resource.gomocdn.com/3704-2019-01-24-10-41-34/soft/face/template/1bXMmkiT.jpg",
    "http://resource.gomocdn.com/e24d-2019-01-24-10-42-09/soft/face/template/a9ZkcULo.jpg",
    "http://resource.gomocdn.com/ebce-2019-01-24-10-45-46/soft/face/template/zjfoHKrg.jpg",
    "http://resource.gomocdn.com/5e44-2019-01-24-10-44-48/soft/face/template/6rqfvQ3s.jpg",
    "http://resource.gomocdn.com/7b67-2019-01-24-10-48-11/soft/face/template/RGiixIE9.jpg",
    "http://resource.gomocdn.com/c34b-2019-01-24-10-49-00/soft/face/template/oxBUt8oD.jpg",
    "http://resource.gomocdn.com/1f86-2019-01-24-10-49-38/soft/face/template/gz0FzqkE.jpg",
    "http://resource.gomocdn.com/d8a4-2019-01-24-10-50-25/soft/face/template/Zm1j5Qte.jpg",
    "http://resource.gomocdn.com/f8b2-2019-01-24-10-51-20/soft/face/template/SaDwLzBI.jpg",
    "http://resource.gomocdn.com/59d7-2019-01-24-10-52-02/soft/face/template/Wm9qVs5A.jpg",
    "http://resource.gomocdn.com/908f-2019-01-24-10-52-50/soft/face/template/lw29952R.jpg"
]
ym = [
    "http://resource.gomocdn.com/a1db-2019-01-15-19-47-14/soft/face/template/MXYLSO6b.jpg",
    "http://resource.gomocdn.com/caa7-2019-01-18-17-14-10/soft/face/template/Eqp0h9j1.jpg",
    "http://resource.gomocdn.com/0ada-2019-01-18-17-14-36/soft/face/template/yuxWdM3B.jpg",
    "http://resource.gomocdn.com/4c61-2019-01-18-17-15-05/soft/face/template/ZJSPzuMy.jpg",
    "http://resource.gomocdn.com/35ce-2019-01-18-17-15-38/soft/face/template/3tpYY2VJ.jpg",
    "http://resource.gomocdn.com/857c-2019-01-18-17-16-24/soft/face/template/wPt5ZbMF.jpg",
    "http://resource.gomocdn.com/7e38-2019-01-18-17-17-12/soft/face/template/6UCzfHkV.jpg",
    "http://resource.gomocdn.com/70de-2019-01-23-17-35-13/soft/face/template/Z9yH5Es7.jpg",
    "http://resource.gomocdn.com/4e53-2019-01-23-17-41-36/soft/face/template/R6UVgnrm.jpg",
    "http://resource.gomocdn.com/9c65-2019-01-23-17-44-39/soft/face/template/QZaHGg7m.jpg",
    "http://resource.gomocdn.com/40ad-2019-01-23-17-56-50/soft/face/template/Cw0LxG9l.jpg",
    "http://resource.gomocdn.com/7270-2019-01-23-17-57-49/soft/face/template/8giiOLWg.jpg",
    "http://resource.gomocdn.com/b049-2019-01-23-18-11-35/soft/face/template/SgMhLraV.jpg",
    "http://resource.gomocdn.com/38f4-2019-01-23-18-17-01/soft/face/template/PJXmG4Vo.jpg",
    "http://resource.gomocdn.com/133f-2019-01-24-10-33-04/soft/face/template/3761nptR.jpg",
    "http://resource.gomocdn.com/86e7-2019-01-24-10-33-47/soft/face/template/BUpPyoW8.jpg",
    "http://resource.gomocdn.com/7ed5-2019-01-24-10-34-32/soft/face/template/BLohMutu.jpg",
    "http://resource.gomocdn.com/78fe-2019-01-24-10-35-14/soft/face/template/4cIQfjxU.jpg",
    "http://resource.gomocdn.com/2742-2019-01-24-10-35-57/soft/face/template/QVSpE5OY.jpg",
    "http://resource.gomocdn.com/8517-2019-01-24-10-36-42/soft/face/template/zOsNgSgb.jpg",
    "http://resource.gomocdn.com/9db8-2019-01-24-10-37-14/soft/face/template/YfUjcN72.jpg",
    "http://resource.gomocdn.com/b63f-2019-01-24-10-38-11/soft/face/template/m0tIDeh6.jpg",
    "http://resource.gomocdn.com/2581-2019-01-24-11-03-39/soft/face/template/K3kOq5bz.jpg"
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







