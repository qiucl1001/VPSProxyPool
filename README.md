## VPSProxyPool
![](https://img.shields.io/badge/python-3.7%2B-brightgreen) 
![](https://img.shields.io/badge/reids-4.0.9%2B-brightgreen)
![](https://img.shields.io/badge/CentOS-7.6%2B-brightgreen)

ADSL拨号代理池

### 开发环境搭建

#### 客户端

* 到第三方技术栈平台购买vps拨号主机(三大运营商<移动、电信、联通>)建议购买电信，根据需求可以购买多台，
  这种三方平台很多，本项目在[云立方](https://www.yunlifang.cn/)平台购买。
* 购买好需要安装操作系统，有Windows、Linux(ubuntu系列、centos系统)，建议安装CentOS7。
* CentOS系统自带没有python3开发环境，需要自行安装，本项目安装Python3.7.2版本。
* 将该主机设置为代理服务器，本项目配置为TinyProxy代理服务器。

#### 服务器端

* 在阿里云或者腾讯云购买一台具有绑定公网可访问的服务器，本项目在[腾讯云](https://cloud.tencent.com/)
  购买了一台，用来存储拨号代理，并提供获取随机代理的API接口。
* 同样安装CentOS7操作系统，安装、配置Python3.7.2开发环境。
* 在本服务器上安装、配置Redis数据库，用来存储vps拨号主机长生的ip代理。

### 项目部署

* vps拨号主机端
    - ssh登录vps拨号主机：使用**git clone https://github.com/qiucl1001/VPSProxyPool.git**命令将项目代码克隆
    到本地。
    - 项目配置
    ```
    cd VPSProxyPool
    pip install requirements.txt
    vim config.py配置远程腾讯云所在的ip地址<公网可访问的ip地址+端口号>
    ```
* 腾讯云服务器端
    - ssh登录腾讯云服务器：使用**git clone https://github.com/qiucl1001/VPSProxyPool.git**命令将项目代码克隆
    到本地。
    - 项目配置
    ```
    cd VPSProxyPool
    pip install requirements.txt
    vim config.py做项目相关参数配置
    ```
### 启动项目
注意：先启动服务器，在启动拨号主机端

* vps拨号主机端
```
cd VPSProxyPool
python client.py

2020-07-31 14:46:39.759 | INFO     | checker.check:get_proxies:16 - Get Proxies
2020-07-31 14:46:39.762 | INFO     | __main__:start_server:26 - Listening on 8000
2020-07-31 14:46:39.764 | INFO     | checker.check:get_proxies:21 - Proxies Empty!
2020-07-31 14:47:12.667 | INFO     | views.index:post:60 - Receive proxy, 27.8.17.48:8888
2020-07-31 14:47:12.668 | INFO     | views.index:post:65 - Saving proxy To Redis Successfully, 27.8.17.48:8888
2020-07-31 14:47:39.775 | INFO     | checker.check:get_proxies:16 - Get Proxies
2020-07-31 14:47:39.776 | INFO     | checker.check:test_proxy:26 - Testing Proxy, adsl1, 27.8.17.48:8888
2020-07-31 14:47:56.275 | INFO     | checker.check:test_proxy:38 - Valid Proxy, adsl1
2020-07-31 14:48:56.303 | INFO     | checker.check:get_proxies:16 - Get Proxies
2020-07-31 14:48:56.304 | INFO     | checker.check:get_proxies:21 - Proxies Empty!
2020-07-31 14:49:20.945 | INFO     | views.index:post:60 - Receive proxy, 27.10.158.162:8888
2020-07-31 14:49:20.945 | INFO     | views.index:post:65 - Saving proxy To Redis Successfully, 27.10.158.162:8888
2020-07-31 14:49:56.322 | INFO     | checker.check:get_proxies:16 - Get Proxies
2020-07-31 14:49:56.323 | INFO     | checker.check:test_proxy:26 - Testing Proxy, adsl1, 27.10.158.162:8888
2020-07-31 14:50:09.386 | INFO     | checker.check:test_proxy:38 - Valid Proxy, adsl1
... ...

```
* 启动vps拨号主机状态如下图所示：

![Image text](https://raw.githubusercontent.com/qiucl1001/VPSProxyPool/master/images/vps%E6%8B%A8%E5%8F%B7%E7%AB%AF.png)

* 腾讯云服务器端
```
cd VPSProxyPool
python server.py

2020-07-31 14:46:39.759 | INFO     | checker.check:get_proxies:16 - Get Proxies
2020-07-31 14:46:39.762 | INFO     | __main__:start_server:26 - Listening on 8000
2020-07-31 14:46:39.764 | INFO     | checker.check:get_proxies:21 - Proxies Empty!
2020-07-31 14:47:12.667 | INFO     | views.index:post:60 - Receive proxy, 27.8.17.48:8888
2020-07-31 14:47:12.668 | INFO     | views.index:post:65 - Saving proxy To Redis Successfully, 27.8.17.48:8888
2020-07-31 14:47:39.775 | INFO     | checker.check:get_proxies:16 - Get Proxies
2020-07-31 14:47:39.776 | INFO     | checker.check:test_proxy:26 - Testing Proxy, adsl1, 27.8.17.48:8888
2020-07-31 14:47:56.275 | INFO     | checker.check:test_proxy:38 - Valid Proxy, adsl1
2020-07-31 14:48:56.303 | INFO     | checker.check:get_proxies:16 - Get Proxies
2020-07-31 14:48:56.304 | INFO     | checker.check:get_proxies:21 - Proxies Empty!
2020-07-31 14:49:20.945 | INFO     | views.index:post:60 - Receive proxy, 27.10.158.162:8888
2020-07-31 14:49:20.945 | INFO     | views.index:post:65 - Saving proxy To Redis Successfully, 27.10.158.162:8888
2020-07-31 14:49:56.322 | INFO     | checker.check:get_proxies:16 - Get Proxies
2020-07-31 14:49:56.323 | INFO     | checker.check:test_proxy:26 - Testing Proxy, adsl1, 27.10.158.162:8888
2020-07-31 14:50:09.386 | INFO     | checker.check:test_proxy:38 - Valid Proxy, adsl1
... ...

```
* 启动腾讯云服务器端状态如下图所示：
![Image Text](https://raw.githubusercontent.com/qiucl1001/VPSProxyPool/master/images/%E8%85%BE%E8%AE%AF%E4%BA%91%E6%9C%8D%E5%8A%A1%E5%99%A8%E7%AB%AF.png)

* 服务器端Redis数据库ip代理状态，这里保存到14号数据库
    ![Image Text](https://raw.githubusercontent.com/qiucl1001/VPSProxyPool/master/images/proxy1.png)
    
    ![Image Text](https://raw.githubusercontent.com/qiucl1001/VPSProxyPool/master/images/proxy2.png)

### 获取代理代码使用样例

1. 代码样例
```python
import requests


def get_proxy():
    with requests.get(
        url='http://129.28.145.3:8000/random',  # 代理服务器所在地址
        headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
             Chrome/83.0.4103.97 Safari/537.36'
        }
    ) as response:
        if response.status_code == 200:
            proxy = response.text
            return proxy


def get_page_source():
    with requests.post(
        url='https://www.renren.com/prefile...',  # 抓取连接页地址
        headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
             Chrome/83.0.4103.97 Safari/537.36'
        },
        proxies={
            'http': 'http://' + get_proxy(),
            'https': 'https://' + get_proxy()
        }
    ) as response:
        if response.status_code  in [200, 201, 304]:
            html = response.text
            print(html)


if __name__ == '__main__':
    get_page_source()

```
2. GUI样例如下图所示：
![Image Text](https://raw.githubusercontent.com/qiucl1001/VPSProxyPool/master/images/%E8%8E%B7%E5%8F%96ip%E4%BB%A3%E7%90%86.png)
