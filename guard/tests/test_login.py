# -*- coding:utf-8 -*-
# @Time: 2020/5/18 13:45
# @Author: wenqin_zhu
# @File: test_login.py
# @Software: PyCharm

import unittest
import requests
""" 接口调用https协议报错的第一步 """
# requests.packages.urllib3.disable_warnings()
from ddt import ddt, data
from guard.tools.path import SharePath
from guard.datas.login_data import LoginData
from utils.handle_config_yaml import HandleConfigYaml


@ddt
class TestLogin(unittest.TestCase):

    # 读取yaml配置文件
    base_config = HandleConfigYaml(r"{}/env.yaml".format(SharePath.CONFIG_FOLDER)).config

    @classmethod
    def setUpClass(cls):
        cls.response_data = requests.request(method=cls.base_config["env"]["method"],
                                             url=r"http://{}/{}".format(cls.base_config["env"]["ip"], cls.base_config["env"]["login"]),
                                             json={"username": cls.base_config["env"]["username"], "password": cls.base_config["env"]["password"]})

    def test_login_success(self):
        """ 测试用户成功登录 """
        login = LoginData().success_login_data
        # 读取测试地址
        url = f'http://{self.base_config["env"]["ip"]}/{login["api"]}'
        # 读取接口的测试数据
        data = {"username": login["username"], "password": login["password"]}
        res = requests.request(method=login["method"], url=url, json=data)
        # 断言
        self.assertEqual(login["expect"], res.status_code)

    @data(*LoginData().abnormal_login_data)
    def test_login_abnormal(self, login):
        """ 测试用户异常登录 """
        # login = LoginData().abnormal_login_data
        # 读取测试地址
        url = f'http://{self.base_config["env"]["ip"]}/{login["api"]}'
        # 读取接口的测试数据
        data = {"username": login["username"], "password": login["password"]}
        res = requests.request(method=login["method"], url=url, json=data)
        # 断言
        self.assertEqual(login["expect"]["code"], res.json()["code"])
        self.assertEqual(login["expect"]["message"], res.json()["message"])

    def test_login_out_success(self):
        """ 测试用户成功登出 """
        login = LoginData().login_out
        # 读取测试地址
        url = f'http://{self.base_config["env"]["ip"]}/{login["api"]}'
        # 设置cookie，通过前置数据中返回的响应值中获取
        # cookies = {"accessToken": "0727d44074754065b00e353b90f2f9ec"}
        cookies = {"accessToken": self.response_data.json()["accessToken"]}
        res = requests.request(method=login["method"], url=url, cookies=cookies)
        # 断言
        self.assertEqual(login["expect"], res.status_code)

    @unittest.skip("接口调用https协议的解决方法和注意事项")
    def test_login(self):
        """ 测试用户成功登录 """
        url = "https://10.151.3.96/senseguard-oauth2/api/v1/login"
        data = {"username": "zhuwenqin", "password": "888888"}
        """ 接口调用https协议报错的第二步：verify=False """
        res = requests.request(method="post", url=url, json=data, verify=False)
        self.assertEqual(200, res.status_code)


if __name__ == '__main__':
    unittest.main()
