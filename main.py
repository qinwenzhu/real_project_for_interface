# -*- coding:utf-8 -*-
# @Time: 2020/5/18 16:44
# @Author: wenqin_zhu
# @File: main.py
# @Software: PyCharm

import unittest
from utils.HTMLTestRunnerNew import HTMLTestRunner

# 导入需要加入到测试套件中的测试模块
from guard.tests import test_device
# 导入需要加入到测试套件中的测试用例类
from guard.tests.test_device import TestDevice


# TODO 方式一： 加载指定的测试模块并执行
# # 1. 创建测试套件
# my_suite = unittest.TestSuite()
# # 2. 创建测试用例加载器
# load_case = unittest.TestLoader()
# # 通过X.py文件为单位添加测试用例
# my_suite.addTest(load_case.loadTestsFromModule(device_demo))
# # 3. 创建测试运行器
# run_case = unittest.TextTestRunner()
# run_case.run(my_suite)

# TODO 方式二： 加载指定的测试用例名并执行，也可以以列表传入多个测试用例名
# # 1. 创建测试套件
# my_suite = unittest.TestSuite()
#
# # 2. 创建测试用例加载器
# load_case = unittest.TestLoader()
# # 通过X.py文件为单位添加测试用例
# # my_suite.addTest(TestDevice('test_1add_device'))
# cases = [TestDevice('test_1add_device'), TestDevice('test_2delete_device')]
# my_suite.addTests(cases)
#
# # 3. 创建测试运行器
# run_case = unittest.TextTestRunner()
# run_case.run(my_suite)

# TODO 方式三： 实际项目常用的用例加载方式
# 1. 直接调用unittest中的默认用例加载方式，一次性加载所有以 test*.py 的测试用例
# my_suite = unittest.defaultTestLoader.discover(start_dir="guard/tests/")
# # 2. 创建测试运行器
# run_case = unittest.TextTestRunner()
# run_case.run(my_suite)

# TODO 实际工作中：加载所有测试用例并生成HTML格式的测试报告
my_suite = unittest.defaultTestLoader.discover(start_dir="guard/tests/")
with open("report.html", mode="wb") as file:
    run_case = HTMLTestRunner(stream=file, title="guard接口api测试报告",description="针对V2.1标准版的api", tester="zhuwenqin")
    run_case.run(my_suite)
