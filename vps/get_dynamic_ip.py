# coding: utf-8
# author: QCL
# software: PyCharm Professional Edition 2018.2.8
import re
import time
import requests
from loguru import logger
from storages.redisclient import RedisClient
from requests.exceptions import ConnectionError

import sys
sys.path.append('..')
from config import CLIENT_NAME, IFNAME, TEST_URL, ADSL_BASH, PROXY_PORT, ADSL_CYCLE, ADSL_ERROR_CYCLE, SERVER_URL, TOKEN

import platform
if platform.python_version().startswith('2.'):
    import commands as subprocess
elif platform.python_version().startswith('3.'):
    import subprocess
else:
    raise ValueError('python version must be 2 or 3')


class Getter(object):
    """获取动态拨号主机产生的ip"""

    def __init__(self, client_name=CLIENT_NAME):
        """初始化"""
        self.db = RedisClient()
        self.client_name = client_name

    @staticmethod
    def get_ip(if_name=IFNAME):
        """
        获取vps拨号主机产生的ip
        :param if_name: 动态拨号vps主机网卡名称
        :return:
        """
        (status, output) = subprocess.getstatusoutput("ifconfig")
        if 0 == status:
            # ifconfig命令执行成功，构建一个提取ip的正则规则
            pattern = re.compile(if_name + '.*?inet.*?(\d+\.\d+\.\d+\.\d+).*?netmask', re.S)
            result = re.search(pattern, output)
            if result:
                ip = result.group(1)
                return ip

    # def remove_proxy(self):
    #     """
    #     移除redis数据库中的ip代理
    #     :return:
    #     """
    #     self.db.remove(CLIENT_NAME)
    #     print('Successfully Removed Proxy for IP')

    # @staticmethod
    # def test_proxy(proxy):
    #     """
    #     测试代理是否可用
    #     :param proxy: 待测试的代理ip
    #     :return:
    #     """
    #     response = requests.get(url=TEST_URL, proxies={
    #         "http": "http://{}".format(proxy),
    #         "https": "https://{}".format(proxy)
    #     })
    #     if response.status_code == 200:
    #         return True
    #     else:
    #         return False

    # def set_proxy(self, proxy):
    #     """
    #     将测试后可用的ip代理保存到redis数据库中
    #     :param proxy: 待保存的代理ip
    #     :return:
    #     """
    #     if self.db.set(self.client_name, proxy):
    #         # 保存成功
    #         logger.info('Proxy Save Successfully', proxy)

    def run(self):
        """
        拨号主进程启动入口
        :return:
        """
        while True:
            logger.info('ADSL Start, Please Wait')
            # 执行vps动态拨号脚本
            (status, output) = subprocess.getstatusoutput(ADSL_BASH)
            if 0 == status:
                logger.info('ADSL Successfully')
                # 获取动态拨号长生的ip
                ip = self.get_ip()
                if ip:
                    logger.info(f'New IP, {ip}')
                    try:
                        with requests.post(
                            url=SERVER_URL,
                            data={
                                'token': TOKEN,
                                'port': PROXY_PORT,
                                'name': CLIENT_NAME
                            }
                        ) as response:
                            if response.status_code == 200:
                                logger.info(f'Successfully Sent to Server, {SERVER_URL}')
                    except ConnectionError:
                        logger.error(f'Failed to Connect Server, {SERVER_URL}')
                    time.sleep(ADSL_CYCLE)

                else:
                    logger.error('Git IP Failed, Try Again')
                    time.sleep(ADSL_ERROR_CYCLE)
            else:
                logger.error('ADSL Dailing Failed, Please Check')
                time.sleep(ADSL_ERROR_CYCLE)


if __name__ == '__main__':
    g = Getter()
    g.run()



