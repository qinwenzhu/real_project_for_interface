# -*- coding:utf-8 -*-
# @Time: 2019/12/9 18:53
# @Author: wenqin_zhu
# @File: component_requests.py
# @Software: PyCharm

import requests
import json


# 创建会话的形式
class ComRequest(object):

    def __init__(self):
        self.session = requests.Session()

    def send_request(self, url, method, data, header, **kwargs):
        global res
        # print(res)
        if method.upper() == "GET":
            res = self.session.get(url, params=data, **kwargs)
        elif method.upper() == "POST":
            if header["Content-Type"] == "application/json":
                if isinstance(data, str):
                    res = self.session.post(url, json=json.dumps(data), **kwargs)
                else:
                    res = self.session.post(url, json=data, **kwargs)
            elif header["Content-Type"] == "application/x-www-form-urlencoded":
                if isinstance(data, str):
                    res = self.session.post(url, data=json.loads(data), **kwargs)
                else:
                    res = self.session.post(url, data=data, **kwargs)
        else:
            print("其他请求方式，待议！")
        print(res)
        return res


if __name__ == '__main__':
    method = "post"
    url = "http://10.151.3.100/senseguard-oauth2/api/v1/login"
    data = {"username": "apitest", "password": "888888"}
    headers = {"Content-Type": "application/json"}

    my_request = ComRequest()
    response = my_request.send_request(url, method, data, headers)
    print(response.status_code)
