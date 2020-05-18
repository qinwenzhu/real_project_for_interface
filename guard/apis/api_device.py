# -*- coding:utf-8 -*-
# @Time: 2019/12/11 15:44
# @Author: wenqin_zhu
# @File: api_device.py
# @Software: PyCharm

from tools.component_requests import ComRequest
from API.api_login import ApiLogin


class ApiDevice(object):
    # swagger 文档    https://10.151.3.100/senseguard-device-management/swagger-ui.html

    def __init__(self):
        # 创建请求实例对象
        self.my_request = ComRequest()
        # 通过调用登录获取响应体内的cookie
        self.headers = {"accessToken": ApiLogin().login().json()["accessToken"]}
        # 明确请求参数的类型
        self.par_type = {"Content-Type": "application/json"}

    def add_device_group(self):
        """创建设备分组"""
        import random
        i = random.randint(0, 9)
        method = "post"
        url = "http://10.151.3.100/senseguard-device-management/api/v1/device-groups"
        data = {
            "name": f"测试设备组{i}",
            "parentId": 0,
            "remark": "设备组"
        }

        res = self.my_request.send_request(url, method, data, self.par_type, headers=self.headers)
        print(f"创建地图层级响应码：{res.status_code}")
        # print(f"当前创建的楼层id为：{res.json()['floorId']}")
        return res

    def add_device(self):
        """创建楼层"""
        import random
        i = random.randint(0, 9)
        method = "post"
        url = "http://10.151.3.100/senseguard-device-management/api/v1/devices"
        data = {
            "name": f"测试楼层{i}",
            "parentId": "",
            "remark": "地图楼层命名"
        }

        res = self.my_request.send_request(url, method, data, self.par_type, headers=self.headers)
        print(f"创建地图层级响应码：{res.status_code}")
        print(f"当前创建的楼层id为：{res.json()['floorId']}")
        return res


if __name__ == '__main__':
    ApiDevice().add_device_group()
