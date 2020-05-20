# -*- coding:utf-8 -*-
# @Time: 2020/5/20 14:31
# @Author: wenqin_zhu
# @File: device_data.py
# @Software: PyCharm


import uuid


def uuid4_data():
    # 生成随机数据
    return str(uuid.uuid4())


class DeviceData:

    # 设备管理 - 添加设备层级
    add_device_group = {"api": "senseguard-device-management/api/v1/device-groups", "method": "post",
                       "data": {"name": f"DLN-{uuid4_data()}", "parentId": 0, "remark": "从根目录创建同级设备层级"},
                       "expect": 200}

    # # 地图管理 - 修改地图层级
    # update_floor_group = {"api": "senseguard-map-management/api/v1/floor", "method": "put",
    #                    "data": {"floorId": "", "name": "", "remark": "修改地图层级"},
    #                    "expect": 200}

    # 地图管理 - 删除地图层级
    group_id = 1    # 设置默认值为1，实际调用的时候进行字符串的替换
    del_device_group = {"api": "senseguard-device-management/api/v1/device-groups/groupId", "method": "delete", "expect": 200}
