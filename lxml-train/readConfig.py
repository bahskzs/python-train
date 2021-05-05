# -*- coding: utf-8 -*-

"""
读取配置文件
Created on 2021/05/05

@author:bahskzs

"""

import configparser

#  实例化configParser对象
config = configparser.ConfigParser()

# read读取ini文件,设定编解码方式
config.read('config.ini', encoding='utf8')


class ReadConfig:
    def getConfigValue(self):
        return config.get('DATABASE', self)
