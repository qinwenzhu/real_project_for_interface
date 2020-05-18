# -*- coding:utf-8 -*-
# @Time: 2019/12/9 20:20
# @Author: wenqin_zhu
# @File: test_floor.py
# @Software: PyCharm

import unittest
import requests
from guard.tools.path import SharePath
from utils.handle_config_yaml import HandleConfigYaml


class TestFloor(unittest.TestCase):

    # 读取yaml配置文件
    base_config = HandleConfigYaml(r"{}/env.yaml".format(SharePath.CONFIG_FOLDER)).config

    @classmethod
    def setUpClass(cls):
        cls.response_data = requests.request(method=cls.base_config["env"]["method"],
                                             url=r"http://{}/{}".format(cls.base_config["env"]["ip"], cls.base_config["env"]["login"]),
                                             json={"username": cls.base_config["env"]["username"], "password": cls.base_config["env"]["password"]})
        cls.cookies = {"cookies": cls.response_data.json()["accessToken"]}

    @classmethod
    def tearDownClass(cls):
        requests.request(method=cls.base_config["env"]["method"],
                         url=r"http://{}/{}".format(cls.base_config["env"]["ip"], cls.base_config["env"]["login_out"]),
                         cookies=cls.cookies)

    def test_add_floor(self):
        # 测试添加地图层级分组
        pass

    def test_delete_floor(self):
        # 测试删除地图层级分组
        pass


if __name__ == '__main__':
    unittest.main()
