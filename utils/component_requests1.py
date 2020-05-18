# -*- coding:utf-8 -*-
# @Time: 2019/11/27 10:51
# @Author: wenqin_zhu
# @File: component_requests.py
# @Software: PyCharm

import requests


"""
针对不同请求的封装
针对http/https的分情况处理
针对携带token的session会话
"""


class ComRequest(object):

    def __init__(self):
        self.session = requests.Session()
        pass

    def main(self, method, url, data):
        if "https" in url:
            if method.upper() == "GET":
                self.session.request(method, url, params=data, verify=False)
            elif method.upper() == "POST":
                if isinstance(data, dict):
                    return self.session.request(method, url, data=data, verify=False)
                    # return requests.request(method, url, data=data, verify=False)
                else:
                    self.session.request(method, url, json=data, verify=False)
            else:
                print("待扩展 -- 如：put请求和delete请求！")
        else:
            if method.upper() == "GET":
                self.session.request(method, url, params=data)
            elif method.upper() == "POST":
                if isinstance(data, dict):
                    self.session.request(method, url, data=data)
                else:
                    self.session.request(method, url, json=data)
            else:
                print("待扩展 -- 如：put请求和delete请求！")


if __name__ == '__main__':
    pass
