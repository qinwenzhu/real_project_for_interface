# -*- coding:utf-8 -*-
# @Time: 2020/5/19 10:27
# @Author: wenqin_zhu
# @File: floor_data.py
# @Software: PyCharm

import uuid


def uuid4_data():
    # 生成随机数据
    return str(uuid.uuid4())


class FloorData:

    # 地图管理 - 添加地图层级
    add_floor_group = {"api": "senseguard-map-management/api/v1/floor", "method": "post",
                       "data": {"name": f"FLN-{uuid4_data()}", "parentId": "", "remark": "从根目录创建同级地图层级"},
                       "expect": 200}

    # 地图管理 - 删除地图层级
    floor_id = 1    # 设置默认值为1，实际调用的时候进行字符串的替换
    state = 0       # state默认状态为0，强制删除需要设置state的值为1
    del_floor_group = {"api": f"senseguard-map-management/api/v1/floor/floor_id/{state}", "method": "delete", "expect": 200}
