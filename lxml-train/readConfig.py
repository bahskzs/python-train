# -*- coding: utf-8 -*-

import configparser
import os

"""
读取配置文件
Created on 2021/05/05

@author : bahskzs

"""


class ReadConfig:
    # def getConfigValue(self):
    #     return config.get('DATABASE', self)

    def __init__(self, filepath=None):
        if filepath:
            config_path = filepath
        else:
            root_dir = os.path.dirname(os.path.abspath('.'))
            config_path = "config.ini"
        self.cf = configparser.ConfigParser()
        self.cf.read(config_path, encoding='utf8')

    def get_db(self, param):
        value = self.cf.get("DATABASE", param)
        return value


if __name__ == '__main__':
    test = ReadConfig()
    t = test.get_db("host")
    print(t)