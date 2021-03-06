# -*- coding:utf-8 -*-
# @Time: 2019/12/9 20:20
# @Author: wenqin_zhu
# @File: test_floor.py
# @Software: PyCharm

import unittest
from guard.apis.api_floor import Floor
from guard.datas.floor_data import FloorData


class TestFloor(unittest.TestCase):

    def test_1add_floor(self):
        # 定义全局变量，进行参数复用
        global add_res

        # 测试添加地图层级分组
        add_res = Floor().add_floor_group()
        # 断言
        self.assertEqual(FloorData().add_floor_group["expect"], add_res.status_code)

    def test_2update_floor(self):
        # 测试添加地图层级分组
        update_res = Floor().update_floor_group(add_res.json()["floorId"], add_res.json()["name"])
        # 断言
        self.assertEqual(FloorData().update_floor_group["expect"], update_res.status_code)

    def test_3delete_floor(self):

        # 测试删除地图层级分组
        del_res = Floor().del_floor_group(add_res.json()["floorId"])
        # 断言
        self.assertEqual(FloorData().del_floor_group["expect"], del_res.status_code)


if __name__ == '__main__':
    unittest.main()
