# -*- coding:utf-8 -*-
# @Time: 2019/11/27 10:29
# @Author: wenqin_zhu
# @File: test_login4.py
# @Software: PyCharm

import requests
import random


from company_script.login import Login


class AddDevice(Login):

    global i
    i = random.randint(0, 9)

    def add_floor(self, parent_id):
        """创建楼层"""
        method = "post"
        url = "http://10.151.3.100/senseguard-map-management/api/v1/floor"
        data = {
            "name": f"测试楼层 {self.i}",
            "parentId": parent_id,
            "remark": "地图楼层命名"
        }
        res = self.session.request(method, url, json=data, headers=self.cookie)
        print(res.status_code)
        return res.json()["name"]

    def is_top_floor(self, parentId):
        """判断是否创建顶级楼层"""
        if parentId is None:
            # 创建顶级楼层
            self.name = self.add_floor(parentId)
        else:
            # 创建指定父楼层的子楼层 1、通过调用-楼层列表接口-获取所有楼层列表信息

            result = self.get_floor_list()
            for floor in result:
                if self.name == floor["name"]:
                    parentId = floor["id"]
            res = self.add_floor(parentId)
            print(res.status_code)
            print(res.json())

    def get_floor_list(self):
        method = "post"
        url = "http://10.151.3.100/senseguard-map-management/api/v1/floor/list"
        data = {
            "name": "",
            "parentId": 0,
            "remark": ""
        }

        res = self.session.request(method, url, json=data, headers=self.cookie)
        print(res.status_code)
        print(res.json()["data"])
        return res.json()["data"]

    def add_map(self):
        pass

    def add_device(self):
        """
        添加设备分组 - 添加设备《需要添加地图 - 添加地图分组 - 添加地图》
        """
        method = "post"
        url = "http://10.151.3.100/senseguard-device-management/api/v1/devices"
        """
        "deviceRunType": 4,   4-DLC
        """
        data = {
            "ID": "VA-ESCC-AA0121",
            "autoReboot": 0,
            "blackListOpen": 0,
            "blackListTip": "string",
            "buzzerStatus": 0,
            "certificateThreshold": 0,
            "codeType": 1,
            "deviceRunType": 4,
            "deviceType": 1,
            "fillLight": 0,
            "firmId": 0,
            "floorId": 1,
            "gpioA": 0,
            "gpioB": 0,
            "gpioC": 0,
            "groupId": 1,
            "ip": "string",
            "keepDoorOpenDuration": 0,
            "languageType": 0,
            "liveness": 0,
            "livenessThreshold": 0,
            "mode": 0,
            "name": "A-ESCC-AA0121（大华）[枪机]",
            "networkRelayAddress": "string",
            "noSenseIp": "string",
            "noSensePort": 0,
            "noSenseSwitch": 0,
            "openDoorType": 0,
            "openInterval": 0,
            "passDeviceType": 0,
            "passPassword": "string",
            "passUsername": "string",
            "password": "string",
            "point": "string",
            "port": 8080,
            "protocolType": "TCP",
            "rebootTime": "string",
            "recognitionDistance": 0,
            "rtspAddress": "rtsp://username:password@ip:port",
            "showUserInfo": "string",
            "showUserName": 0,
            "standbyOpen": 0,
            "streamType": "RTSP",
            "useMode": 0,
            "useShowAvatar": 0,
            "userIds": [
                0
            ],
            "username": "string",
            "verifyFaultTip": "string",
            "verifySuccessTip": "string",
            "verifyThreshold": 0,
            "voiceBroadcast": 0,
            "waitTime": 0,
            "welcomeTip": "string",
            "wiganInput": 0
        }
        pass


if __name__ == '__main__':
    myself = AddDevice()
    myself.add_floor("")
    # myself.add_floor("")
    # myself.get_floor_list()
