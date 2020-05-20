# -*- coding:utf-8 -*-
# @Time: 2020/5/20 14:28
# @Author: wenqin_zhu
# @File: api_device.py
# @Software: PyCharm

import requests
from guard.tools.login import Login
from guard.tools.path import SharePath
from guard.datas.device_data import DeviceData
from utils.handle_config_yaml import HandleConfigYaml


class Device:
    """
    设备管理模块：创建地图层级、修改地图层级、删除地图层级
    添加设备、修改设备、删除设备
    """

    # 读取yaml，当前运行环境的相关配置文件
    base_config = HandleConfigYaml(r"{}/env.yaml".format(SharePath.CONFIG_FOLDER)).config
    # 先调用登录接口，获取响应值中返回的cookies
    cookies = Login().login()

    # 添加设备层级分组
    def add_device_group(self):
        # 读取添加地图层级的data
        add_device = DeviceData().add_device_group

        url = f'http://{self.base_config["env"]["ip"]}/{add_device["api"]}'
        res = requests.request(method=add_device["method"], url=url, json=add_device["data"],
                               cookies=self.cookies)
        print(f"返回响应结果：{res.json()}")
        return res

    # 删除设备分组
    def del_device_group(self, device_group_id):
        # 读取删除地图层级的data
        del_device = DeviceData().del_device_group

        url_link = del_device["api"].replace("groupId", str(device_group_id))
        url = f'http://{self.base_config["env"]["ip"]}/{url_link}'
        res = requests.request(method=del_device["method"], url=url, cookies=self.cookies)
        print(f"返回响应结果：{res.json()}")
        return res


if __name__ == '__main__':
    res = Device().add_device_group()
    a = res.json()
    Device().del_device_group(a["groupId"])
