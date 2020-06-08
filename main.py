# -*- coding:utf-8 -*-
# @Time: 2020/5/18 16:44
# @Author: wenqin_zhu
# @File: main.py
# @Software: PyCharm

import unittest

from guard.tests import test_device
from guard.tests import test_login
from guard.tests import test_floor
# 导入第三方插件   HTMLTestRunner


# 创建测试套件
my_suite = unittest.TestSuite()

# 加载测试类
load_case = unittest.TestLoader()
# load_case.loadTestsFromModule(test_device)
# 将加载完成的目标测试用例module放进测试套件内
# 将单个需要执行的测试模块添加到测试套件中
my_suite.addTest(load_case.loadTestsFromModule(test_device))
# case = loader.discover("guard/tests")

# 一次性加载测试用例列表到测试套件中
# cases = [test_device, test_login, test_floor]
# my_suite.addTests(cases)

# 创建测试运行
run_case = unittest.TextTestRunner()
run_case.run(my_suite)

# 生成测试报告
# HTMLTestRunner

# if __name__ == '__main__':
#     unittest.main()
