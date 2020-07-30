# coding: utf-8
# author: QCL
# software: PyCharm Professional Edition 2018.2.8
import redis
import random
from loguru import logger

import sys
sys.path.append('..')
from config import REDIS_HOST, REDIS_PORT, REDIS_PASSWORD, PROXY_KEY, REDIS_DB


class RedisClient(object):
    """定义一个连接redis数据库的客户端类"""

    def __init__(self, host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD, db=REDIS_DB, proxy_key=PROXY_KEY):
        """
        初始化
        :param host: redis数据库ip地址
        :param port: redis数据库端口
        :param password: redis数据库登录密码
        :param proxy_key: 哈希表名称
        """
        self.db = redis.StrictRedis(host=host, port=port, password=password, db=db, decode_responses=True)
        self.proxy_key = proxy_key

    def set(self, name, proxy):
        """
        设置代理
        :param name:主机名称
        :param proxy: ip代理
        :return: 设置的结果
        """
        return self.db.hset(self.proxy_key, name, proxy)

    def get(self, name):
        """
        获取代理
        :param name: 主机名称
        :return: ip代理
        """
        return self.db.hget(self.proxy_key, name)

    def count(self) ->int:
        """
        获取redis数据库中存储的ip代理总数
        :return: 代理总数
        """
        return self.db.hlen(self.proxy_key)

    def remove(self, name) ->int:
        """
        删除代理
        :param name:主机名称
        :return: 删除结果：1表示删除成功 0表示删除失败
        """
        return self.db.hdel(self.proxy_key, name)

    def names(self) ->list:
        """
        获取所有的主机名称
        :return: 以列表的形式返回redis数据库中所有的主机名称
        """
        return self.db.hkeys(self.proxy_key)

    def proxies(self) ->list:
        """
        获取redis数据库中存储的所有ip代理
        :return: 以列表的形式返回redis数据库中所有的ip代理
        """
        return self.db.hvals(self.proxy_key)

    def random(self) ->str:
        """
        从redis数据库中随机获取一个代理
        :return: 一个ip代理
        """
        proxy_list = self.proxies()
        if proxy_list:
            proxy = random.choice(proxy_list)
            logger.info(f'Successfully Get Random Proxy From Redis: {proxy}')
            return proxy

    def all(self) ->dict:
        """
        获取所有字典 e.g: {"adsl1": "192.168.1.100:8888", "adsl2": "192.168.1.101:6800", ...}
        :return:
        """
        return self.db.hgetall(self.proxy_key)


if __name__ == '__main__':
    r = RedisClient()
    r.set('adsl1', '192.168.1.1:8888')
    r.set('adsl2', '192.168.1.2:6666')
    r.set('adsl3', '192.168.1.3:7777')

    # print(r.all()) # ---> {'adsl1': '192.168.1.1:8888', 'adsl2': '192.168.1.2:6666', 'adsl3': '192.168.1.3:7777'}
    # print(r.proxies())  # ---> ['192.168.1.1:8888', '192.168.1.2:6666', '192.168.1.3:7777']
    # print(r.random())  # ---> 192.168.1.2:6666
    # print(r.names())  # ---> ['adsl1', 'adsl2', 'adsl3']
    # res = r.remove('adsl3')
    # print(res, type(res))  # ---> 1 <class 'int'>






