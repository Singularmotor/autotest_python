#coding = utf-8
#running in python3.6

import os
import time

GP_1_natural = [
    'adb shell am broadcast -a com.android.vending.INSTALL_REFERRER --es referrer "utm_source=google-play\&zerokey_click_id=\&zerokey_channel=14449_"',
    'adb shell am broadcast -a com.android.vending.INSTALL_REFERRER --es referrer "utm_source=google-play\&cskey_click_id=\&cskey_channel=14449_"'
]  #gp自然（-1）

GP_1_na_or_no8 = [
    'adb shell am broadcast -a com.android.vending.INSTALL_REFERRER --es referrer "utm_source=null\&zerokey_click_id=\&zerokey_channel=14449_"'
]  #gp自然（-1）/非gp自然（8）：（非gp自然：gp版本≥6.8.24;gp自然：gp版本<6.8.24）

Natural0 = [
    'adb shell am broadcast -a com.android.vending.INSTALL_REFERRER --es referrer "utm_source=appflood\&utm_medium=banner\&utm_campaign=appflood\&zerokey_channel\&gokey_channel=\&from_3g_channel=organic"'
]  #自然带量：（0）

No_natural7 = [
    'adb shell am broadcast -a com.android.vending.INSTALL_REFERRER --es referrer "utm_source=appflood\&utm_medium=banner\&cskey_click_id\&from_3g_chadnnel=organic"',
    'adb shell am broadcast -a com.android.vending.INSTALL_REFERRER --es referrer "utm_source=appflood\&utm_medium=banner\&utm_campaign=appflood\&zerokey_channel\&cskey_channel=\&from_3G_channel=anything"',
    'adb shell am broadcast -a com.android.vending.INSTALL_REFERRER --es referrer "utm_source=suing\&from_3G_channel=withCount"',
    'adb shell am broadcast -a com.android.vending.INSTALL_REFERRER --es referrer "utm_source=appflood\&utm_medium=banner\&utm_campaign=appflood\&zerokey_channel\&cskey_channel=1452"',
    'adb shell am broadcast -a com.android.vending.INSTALL_REFERRER --es referrer "utm_source=not%20set\&utm_medium=banner\&utm_campaign=appflood\&zerokey_channel\&cskey_channel="',
    'adb shell am broadcast -a com.android.vending.INSTALL_REFERRER --es referrer "utm_source=4568\&from_3g_channel"'
]  #非自然带量：（7）

GA1 = [
    'adb shell am broadcast -a com.android.vending.INSTALL_REFERRER --es referrer "utm_source=appflood\&zerokey_click_id=\&zerokey_channel=14449_\&from_3g_channel=organic"',
    'adb shell am broadcast -a com.android.vending.INSTALL_REFERRER --es referrer "utm_source=not%20set\&utm_medium=banner\&utm_campaign=appflood_speed\&cskey_click_id=5a49def5b4bfab58e618b191fe7704ed011\&cskey_channel=153_"'
]  #GA买量(1)

AF1 = [
    'adb shell am broadcast -a com.android.vending.INSTALL_REFERRER --es referrer "utm_source=&zerokey_click_id=&af_tranid=AL7oybEZ6cvS07b-fDV5nA&pid=mundomedia_int&c=CD25730_212537703&clickid=9ad8dbfe-2f0b-5009-b692-94e803b13a60&af_siteid=CD25730_212537703&campaignid=e2c4035474r2w2&af_sub1=CD25730&af_status=Non-organic&media_source=aa &campaign=xm_ediakey&is_fb=false&agency=ddd"',
    'adb shell am broadcast -a com.android.vending.INSTALL_REFERRER --es referrer "utm_source=appflood&zerokey_channel=14449_&af_tranid=AL7oybEZ6cvS07b-fDV5nA&pid=mundomedia_int&c=CD25730_212537703&clickid=9ad8dbfe-2f0b-5009-b692-94e803b13a60&af_siteid=CD25730_212537703&campaignid=e2c4035474r2w2&af_sub1=CD25730&af_status=Non-organic&media_source=aa &campaign=xmediazerokey&is_fb=false&agency="',
    'adb shell am broadcast -a com.android.vending.INSTALL_REFERRER --es referrer "utm_source=appflood&zerokey_channel=14449_&af_tranid=AL7oybEZ6cvS07b-fDV5nA&pid=mundomedia_int&c=CD25730_212537703&clickid=9ad8dbfe-2f0b-5009-b692-94e803b13a60&af_siteid=CD25730_212537703&campaignid=e2c4035474r2w2&af_sub1=CD25730&af_status=Non-organic&media_source=aa &campaign=xmediazerokey&agency=null"'
]  #GA广播模拟AF普通买量,AF普通买量，类型（1）

AF_FB2 = [
    'adb shell am broadcast -a com.android.vending.INSTALL_REFERRER --es referrer "utm_source=appflood&zerokey_click_id=&zerokey_channel=14449_&af_tranid=AL7oybEZ6cvS07b-fDV5nA&pid=mundomedia_int&c=CD25730_212537703&clickid=9ad8dbfe-2f0b-5009-b692-94e803b13a60&af_siteid=CD25730_212537703&campaignid=e2c4035474r2w2&af_sub1=CD25730&af_status=Non-organic&media_source=Facebook Ads&campaign=xmediazerokey_&is_fb=true"',
    'adb shell am broadcast -a com.android.vending.INSTALL_REFERRER --es referrer "utm_source=not%20set&af_tranid=AL7oybEZ6cvS07b-fDV5nA&pid=mundomedia_int&c=CD25730_212537703&clickid=9ad8dbfe-2f0b-5009-b692-94e803b13a60&af_siteid=CD25730_212537703&campaignid=e2c4035474r2w2&af_sub1=CD25730&af_status=Non-organic&media_source=Facebook Ads&campaign=xmxxmxlihahhd_ediazerokey&is_fb=true"'
]  #GA广播模拟AF FB自投（2）

AF_FBN3 = [
    'adb shell am broadcast -a com.android.vending.INSTALL_REFERRER --es referrer "utm_source=not%20set&af_tranid=AL7oybEZ6cvS07b-fDV5nA&pid=mundomedia_int&c=CD25730_212537703&clickid=9ad8dbfe-2f0b-5009-b692-94e803b13a60&af_siteid=CD25730_212537703&campaignid=e2c4035474r2w2&af_sub1=CD25730&af_status=Non-organic&media_source=Facebook Ads&campaign=&is_fb=true"',
    'adb shell am broadcast -a com.android.vending.INSTALL_REFERRER --es referrer "utm_source=appflood&zerokey_click_id=&zerokey_channel=14449_&af_tranid=AL7oybEZ6cvS07b-fDV5nA&pid=mundomedia_int&c=CD25730_212537703&clickid=9ad8dbfe-2f0b-5009-b692-94e803b13a60&af_siteid=CD25730_212537703&campaignid=e2c4035474r2w2&af_sub1=CD25730&af_status=Non-organic&media_source=Facebook Ads&campaign=xm&is_fb=true"'
]  #GA广播模拟AF FB非自投（3）

AF_aw6 = [
    'adb shell am broadcast -a com.android.vending.INSTALL_REFERRER --es referrer "utm_source=appflood\&gokey_channel=\&gokey_click_id=14449\&af_tranid=AL7oybEZ6cvS07b-fDV5nA\&agency=123\&campaignid=111\&media_source=googleadwords_int"',
    'adb shell am broadcast -a com.android.vending.INSTALL_REFERRER --es referrer "utm_source=appflood\&gokey_channel=\&gokey_click_id=14449\&af_tranid=AL7oybEZ6cvS07b-fDV5nA\&agency=123\&campaignid=111\&c=CD25730_212537703\&clickid=9ad8dbfe\&af_status=Non-organic\&af_siteid=CD25730_212537703\&media_source=googleadwords_int"'
]  #GA广播模拟AF adwords非自投（6）

AF_aw4 = [
    'adb shell am broadcast -a com.android.vending.INSTALL_REFERRER --es referrer "utm_source=appflood\&gokey_channel=\&gokey_click_id=14449\&af_tranid=AL7oybEZ6cvS07b-fDV5nA\&agency=\&campaignid=111\&c=CD25730_212537703\&clickid=9ad8dbfe\&af_status=Non-organic\&af_siteid=CD25730_212537703&is_fb=false\&media_source=googleadwords_int"',
    'adb shell am broadcast -a com.android.vending.INSTALL_REFERRER --es referrer "utm_source=appflood\&gokey_channel=\&gokey_click_id=14449\&af_tranid=AL7oybEZ6cvS07b-fDV5nA\&agency=\&campaignid=111\&media_source=googleadwords_int"'
]  #GA广播模拟AF 模拟adwords自投（4）

AF_aw_GDN = [
    'adb shell am broadcast -a com.android.vending.INSTALL_REFERRER --es referrer "utm_source=appflood\&gokey_channel=\&gokey_click_id=14449\&af_tranid=AL7oybEZ6cvS07b-fDV5nA\&agency=\&campaignid=111\&c=CD25730_212537703\&clickid=9ad8dbfe\&af_status=Non-organic\&af_siteid=CD25730_212537703&is_fb=false\&media_source=googleadwords_int"',
    'adb shell am broadcast -a com.android.vending.INSTALL_REFERRER --es referrer "utm_source=appflood\&gokey_channel=\&gokey_click_id=14449\&af_tranid=AL7oybEZ6cvS07b-fDV5nA\&agency=\&campaignid=111\&media_source=googleadwords_int"',
    'adb shell am broadcast -a com.android.vending.INSTALL_REFERRER --es referrer "utm_source=appflood\&gokey_channel=\&gokey_click_id=14449\&af_tranid=AL7oybEZ6cvS07b-fDV5nA\&agency=123\&campaignid=111\&media_source=googleadwords_int"'
]  #GA广播模拟AF 模拟adwords子渠道GDN（测试时，把campaignid=111修改为客户端传进来的真实campaignid）

all_buychannel = [GP_1_natural,GP_1_na_or_no8,Natural0,No_natural7,GA1,AF1,AF_FB2,AF_FBN3,AF_aw4,AF_aw6]

phone_api = int(os.popen('adb shell getprop ro.build.version.sdk').read()) #get API version of Android phone
loo = str(os.popen('adb shell getprop ro.product.model').read())#get model name of Android phone

phone_model_name = ''
for i in loo:
    if i == '\n':
        pass
    else:
        phone_model_name = phone_model_name+i
#print(phone_model_name)



log_time = time.localtime(time.time())
log_name = str('%s-'%(phone_model_name)+'%s%s%s%s%s%s'%(log_time.tm_year,log_time.tm_mon,log_time.tm_mday,log_time.tm_hour,log_time.tm_min,log_time.tm_sec))
#print(log_name)

#record logat
def fun_buychannel(list):
    buychannel_list = []
    if phone_api >= 26:  # identify which buychannel list should we use
        for x in list:
            y = x + ' -n com.nj.fface/com.appsflyer.MultipleInstallBroadcastReceiver'#"com.nj.fface"修改成自己对应的包名
            buychannel_list.append(y)
        # print('26+')
    else:
        buychannel_list = list
        # print('26-')
    for i in buychannel_list:
        print(i)
    #clear the app
        os.system('adb shell pm clear com.nj.fface')
        time.sleep(1)
    #start the app
        os.system('adb shell am start -n com.nj.fface/com.nj.fface.activity.SplashActivity')#"com.nj.fface"修改成自己对应的包名
        time.sleep(1)
    #set buychannel
        os.system(i)
        time.sleep(17)

def run_log():
    os.popen("adb logcat>%s.txt"%(log_name))


if __name__ == '__main__' :
    for ls in all_buychannel:
        fun_buychannel(ls)








