from sqlalchemy import create_engine
from readConfig import ReadConfig
import base64

"""
Desc : 进行数据库的相关操作

Created on 2021/05/06

@author : bahskzs

"""


class HandleMysql:
    def __init__(self):
        self.data = ReadConfig()

    def conn_mysql(self):
        """连接数据库"""
        connect_info = 'mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=utf8'.format(
                username=self.data.get_db('user'),
                password=base64.b64decode(self.data.get_db('passwd')).decode('ascii'),
                host=self.data.get_db('host'),
                port=self.data.get_db('port'),
                db=self.data.get_db('db'))

        engine = create_engine(connect_info)
        return engine
