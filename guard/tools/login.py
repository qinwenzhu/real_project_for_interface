# -*- coding:utf-8 -*-
# @Time: 2020/5/19 19:52
# @Author: wenqin_zhu
# @File: login.py
# @Software: PyCharm

import requests
from guard.tools.path import SharePath
from utils.handle_config_yaml import HandleConfigYaml


class Login:
    # 读取yaml，当前运行环境的相关配置文件
    base_config = HandleConfigYaml(r"{}/env.yaml".format(SharePath.CONFIG_FOLDER)).config

    def login(self):
        # 调用系统登录接口
        response_data = requests.request(method=self.base_config["env"]["method"],
                                         url=r"http://{}/{}".format(self.base_config["env"]["ip"], self.base_config["env"]["login"]),
                                         json={"username": self.base_config["env"]["username"],
                                               "password": self.base_config["env"]["password"]})
        # 获取接口响应中的cookie
        cookies = {"accessToken": response_data.json()["accessToken"]}
        return cookies
