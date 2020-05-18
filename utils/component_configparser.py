# -*- coding:utf-8 -*-
# @Time: 2019/12/10 10:36
# @Author: wenqin_zhu
# @File: component_configparser.py
# @Software: PyCharm

import configparser


class ComConfig(object):

    def __init__(self, filename):
        self.my_config = configparser.ConfigParser()
        self.my_config.read(filenames=filename, encoding='utf-8')

    def read_config(self, section, option):
        return self.my_config.get(section, option)
