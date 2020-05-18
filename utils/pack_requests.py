# -*- coding:utf-8 -*-
# @Time: 2019/11/29 19:41
# @Author: wenqin_zhu
# @File: pack_requests.py
# @Software: PyCharm

"""
封装 requests 库
~~~~~~~~~~~~~~~~~~~~~
get请求
post请求
put请求
delete请求
data的数据格式转换
"""

import requests
import json


class PackRequests(object):

    def __init__(self):
        # 实例化session会话对象
        self.session = requests.Session()

    def send_request(self, method, url, data, **kwargs):
        """封装get、post、put、delete请求"""
        if method.upper() == "GET":
            self.session.get(url, params=data, **kwargs)
            pass
        elif method.upper() == "POST":
            if isinstance(data, dict):
                # 如果data的类型为dict
                self.session.post(url, data=data, **kwargs)
            else:
                # 否则将data的类型转换成json
                self.session.post(url, json=json.load(data), **kwargs)
        elif method.upper() == "PUT":
            pass
        elif method.upper() == "DELETE":
            pass
        else:
            print("发生错误，请检查请求方法！")

    def __del__(self):
        # 关闭会话连接
        self.session.close()


if __name__ == '__main__':
    pass
