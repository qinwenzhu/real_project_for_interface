# -*- coding:utf-8 -*-
# @Time: 2019/12/9 18:53
# @Author: wenqin_zhu
# @File: component_requests.py
# @Software: PyCharm

import requests
import json


class ComRequest(object):

    def send_request(self, url, method, data=None, parameter_content_type=None,**kwargs):
        if method.upper() == "GET":
            res = requests.get(url, params=data, **kwargs)
        elif method.upper() == "POST":
            if parameter_content_type["Content-Type"] == "application/json":
                if isinstance(data, str):
                    res = requests.post(url, json=json.dumps(data), **kwargs)
                else:
                    res = requests.post(url, json=data, **kwargs)
            elif parameter_content_type["Content-Type"] == "application/x-www-form-urlencoded":
                if isinstance(data, str):
                    res = requests.post(url, data=json.loads(data), **kwargs)
                else:
                    res = requests.post(url, data=data, **kwargs)
        elif method.upper() == "DELETE":
            res = requests.delete(url, **kwargs)
        else:
            print("其他请求方式，待议！")
        return res


if __name__ == '__main__':
    method = "post"
    url = "http://10.151.3.100/senseguard-oauth2/api/v1/login"
    data = {"username": "apitest", "password": "888888"}
    headers = {"Content-Type": "application/json"}

    my_request = ComRequest()
    response = my_request.send_request(url, method, data, headers)
    print(response.status_code)
