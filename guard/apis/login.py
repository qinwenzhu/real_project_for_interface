# -*- coding:utf-8 -*-
# @Time: 2019/11/29 10:54
# @Author: wenqin_zhu
# @File: login.py
# @Software: PyCharm

import requests


class Login(object):

    def __init__(self):
        method = "post"
        url = "http://10.151.3.100/senseguard-oauth2/api/v1/login"
        data = {"username": "apitest", "password": "888888"}

        self.session = requests.Session()
        res = self.session.request(method, url, json=data)

        self.cookie = {
            "accessToken": res.json()['accessToken']
        }


if __name__ == '__main__':
    pass
