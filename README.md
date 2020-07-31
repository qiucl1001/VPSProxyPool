## VPSProxyPool
![](https://img.shields.io/badge/python-3.7%2B-brightgreen)

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
  手机号联通验证)购买了一台，用来存储拨号代理，并提供获取随机代理的API接口。
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
```
* 腾讯云服务器端
```
cd VPSProxyPool
python server.py
```


