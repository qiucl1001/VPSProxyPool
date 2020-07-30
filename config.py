# coding: utf-8
# author: QCL
# software: PyCharm Professional Edition 2018.2.8
from environs import Env
from loguru import logger

env = Env()

# 动态拨号vps主机网卡名称
IFNAME = env('IFNAME', 'ppp0')
# redis数据库散列表中键名为客户端主机的唯一标识
CLIENT_NAME = env.str('CLIENT_NAME', 'adsl1')
# vps动态拨号脚本
ADSL_BASH = env.str('ADSL_BASH', 'adsl-stop;adsl-start')
# 拨号出错长生异常时从新尝试时间间隔 单位：秒
ADSL_ERROR_CYCLE = env.int('ADSL_ERROR_CYCLE', 5)
# vps动态拨号主机拨号间隔 单位：秒
ADSL_CYCLE = env.int('ADSL_CTCLE', 100)
# proxy pool检测周期 单位：秒
TEST_PROXY_POOL_CYCLE = env.int('TEST_PROXY_POOL_CYCLE', 60)

# Redis数据库IP
REDIS_HOST = env.str('REDIS_HOST', 'localhost')
# Redis数据库端口
REDIS_PORT = env.int('REDIS_PORT', 6379)
# Redis数据库密码, 如无则填None
REDIS_PASSWORD = env.str('REDIS_PASSWORD', None)
# Redis数据库号, 默认为0号数据库
REDIS_DB = env.int('REDIS_DB', 14)

# 代理池键名
PROXY_KEY = env.str('REDIS_KEY', 'adsl')
# 通信秘钥
TOKEN = env.str('TOKEN', 'adsl')
# 验证URL
TEST_URL = env.str('TEST_URL', 'http://httpbin.org/get')
# 检测间隔
TEST_CYCLE = env.int('TEST_CYCLE', 20)

# 服务器端口
SERVER_PORT = env.int('SERVER_PORT', 8000)
SERVER_HOST = env.str('SERVER_HOST', '0.0.0.0')
# 服务器地址
SERVER_URL = env.str('SERVER_URL', 'http://120.27.34.24:8000')

# 代理端口
PROXY_PORT = env.int('PROXY_PORT', 8888)
PROXY_USERNAME = env.str('PROXY_USERNAME', '')
PROXY_PASSWORD = env.str('PROXY_PASSWORD', '')


# log日志文件配置
logger.add(env.str('LOG_RUNTIME_FILE', 'runtime.log'), level='DEBUG', rotation='1 week', retention='20 days')
logger.add(env.str('LOG_ERROR_FILE', 'error.log'), level='ERROR', rotation='1 week')

