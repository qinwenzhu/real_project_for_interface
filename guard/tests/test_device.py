# -*- coding:utf-8 -*-
# @Time: 2020/5/20 14:53
# @Author: wenqin_zhu
# @File: test_device.py
# @Software: PyCharm
import unittest
from guard.apis.api_device import Device
from guard.datas.device_data import DeviceData


class TestDevice(unittest.TestCase):

    def test_1add_device(self):
        # 定义全局变量，进行参数复用
        global add_res

        # 测试添加地图层级分组
        add_res = Device().add_device_group()
        # 断言
        self.assertEqual(DeviceData().add_device_group["expect"], add_res.status_code)

    def test_3delete_device(self):

        # 测试删除地图层级分组
        del_res = Device().del_device_group(add_res.json()["groupId"])
        # 断言
        self.assertEqual(DeviceData().del_device_group["expect"], del_res.status_code)


if __name__ == '__main__':
    unittest.main()
