# -*- coding:utf-8 -*-
# @Time: 2019/12/10 13:03
# @Author: wenqin_zhu
# @File: api_login.py
# @Software: PyCharm

from tools.component_requests import ComRequest
from tools.component_configparser import ComConfig
from tools.common_os import BASE_CON


class ApiLogin(object):
    """登录
        Swagger文档：https://10.151.3.100/senseguard-oauth2/swagger-ui.html
    """

    def __init__(self):
        self.my_request = ComRequest()
        self.my_config = ComConfig(BASE_CON)

    def login(self):
        method = "post"
        # url = "http://10.151.3.100/senseguard-oauth2/api/v1/login"
        host = self.my_config.read_config("base", "host")
        print(host)
        url = f"http://{host}/senseguard-oauth2/api/v1/login"
        data = {"username": "apitest", "password": "888888"}
        par_type = {"Content-Type": "application/json"}

        res = self.my_request.send_request(url, method, data, par_type)
        print(f"登录响应码：{res.status_code}")

        return res


if __name__ == '__main__':
    # 测试登录
    ApiLogin().login()
