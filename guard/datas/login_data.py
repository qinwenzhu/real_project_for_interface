# -*- coding:utf-8 -*-
# @Time: 2020/5/18 15:19
# @Author: wenqin_zhu
# @File: login_data.py
# @Software: PyCharm


class LoginData:
    # 用户登录 - 正常登录
    success_login_data = {"api": "senseguard-oauth2/api/v1/login", "method": "post", "username": "zhuwenqin",
                          "password": "888888", "expect": 200}

    # 异常测试数据 - 用户名和密码的非空校验/错误登录
    abnormal_login_data = [{"api": "senseguard-oauth2/api/v1/login", "method": "post", "username": "",
                           "password": "888888", "expect": {"code": "401019", "message": "用户名或者密码为空"}},
                           {"api": "senseguard-oauth2/api/v1/login", "method": "post", "username": "zhuwenqin",
                            "password": "", "expect": {"code": "401019", "message": "用户名或者密码为空"}},
                           {"api": "senseguard-oauth2/api/v1/login", "method": "post", "username": "string",
                            "password": "string", "expect": {"code": "401003", "message": "用户不存在"}}]

    # 用户登出 - 正常登出
    login_out = {"api": "senseguard-oauth2/api/v1/logout", "method": "post", "expect": 200}
