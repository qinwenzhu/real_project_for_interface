# -*- coding:utf-8 -*-
# @Time: 2020/5/19 19:30
# @Author: wenqin_zhu
# @File: api_floor.py
# @Software: PyCharm


import requests
from guard.tools.login import Login
from guard.tools.path import SharePath
from guard.datas.floor_data import FloorData
from utils.handle_config_yaml import HandleConfigYaml


class Floor:
    """
    地图管理模块：创建地图层级、修改地图层级、删除地图层级
    楼层列表、是否子楼层、地图上传、删除地图等
    """

    # 读取yaml，当前运行环境的相关配置文件
    base_config = HandleConfigYaml(r"{}/env.yaml".format(SharePath.CONFIG_FOLDER)).config
    # 先调用登录接口，获取响应值中返回的cookies
    cookies = Login().login()

    # 创建地图分组
    def add_floor_group(self):
        # 读取添加地图层级的data
        add_floor = FloorData().add_floor_group

        url = f'http://{self.base_config["env"]["ip"]}/{add_floor["api"]}'
        res = requests.request(method=add_floor["method"], url=url, json=add_floor["data"],
                               cookies=self.cookies)
        print(f"返回响应结果：{res.json()}")
        return res

    # 删除地图分组
    def del_floor_group(self, floor_id):
        # 读取删除地图层级的data
        del_floor = FloorData().del_floor_group

        url_link = del_floor["api"].replace("floor_id", str(floor_id))
        url = f'http://{self.base_config["env"]["ip"]}/{url_link}'
        res = requests.request(method=del_floor["method"], url=url, cookies=self.cookies)
        print(f"返回响应结果：{res.json()}")
        return res


if __name__ == '__main__':
    # Floor().add_floor_group()
    Floor().del_floor_group()
