# -*- coding:utf-8 -*-
# @Time: 2019/12/10 17:34
# @Author: wenqin_zhu
# @File: api_floor.py
# @Software: PyCharm

from tools.component_requests import ComRequest
from API.api_login import ApiLogin


class ApiFloor(object):

    def __init__(self):
        # 创建请求实例对象
        self.my_request = ComRequest()
        # 通过调用登录获取响应体内的cookie
        self.headers = {"accessToken": ApiLogin().login().json()["accessToken"]}
        # 明确请求参数的类型
        self.par_type = {"Content-Type": "application/json"}

    def add_floor(self):
        """创建楼层"""
        import random
        i = random.randint(0, 9)
        method = "post"
        url = "http://10.151.3.100/senseguard-map-management/api/v1/floor"
        data = {
            "name": f"测试楼层{i}",
            "parentId": "",
            "remark": "地图楼层命名"
        }

        res = self.my_request.send_request(url, method, data, self.par_type, headers=self.headers)
        print(f"创建地图层级响应码：{res.status_code}")
        print(f"当前创建的楼层id为：{res.json()['floorId']}")
        return res

    def upload_map(self):
        """上次层级地图"""
        import random
        i = random.randint(0, 9)
        method = "get"

        # 通过调用-添加地图层级-获取楼层id
        floor_id = self.add_floor()
        floorId = floor_id.json()["floorId"]

        url = f"http://10.151.3.100/senseguard-map-management/api/v1//floor/map/{floorId}"
        data = {
            "name": f"测试楼层{i}",
            "parentId": "",
            "remark": "地图楼层命名"
        }

        res = self.my_request.send_request(url, method, data, self.par_type, headers=self.headers)
        print(f"创建地图层级响应码：{res.status_code}")
        return res

    def delete_floor(self, id, state):
        """删除楼层"""
        method = "delete"
        # 通过调用-添加地图层级-获取楼层id
        # floor_id = self.add_floor()
        # id = floor_id.json()["floorId"]
        # state = 0
        url = f"http://10.151.3.100/senseguard-map-management/api/v1/floor/{id}/{state}"

        res = self.my_request.send_request(url, method, self.par_type, headers=self.headers)
        print(f"删除指定地图层级响应码：{res.status_code}")
        return res

    def query_floor_list(self):
        """查询楼层列表"""
        method = "post"
        url = "http://10.151.3.100/senseguard-map-management/api/v1/floor/list"
        data = {
            "name": "",
            "parentId": "",
            "remark": ""
        }

        res = self.my_request.send_request(url, method, data, self.par_type, headers=self.headers)
        print(f"查询地图层级列表响应码：{res.status_code}")
        return res

    # def delete_appoint_floor(self, id):
    #     pass


if __name__ == '__main__':
    # ApiFloor().add_floor()
    # ApiFloor().delete_floor()
    ApiFloor().upload_map()
    # ApiFloor().query_floor_list()
