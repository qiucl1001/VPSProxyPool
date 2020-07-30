# coding: utf-8
# author: QCL
# software: PyCharm Professional Edition 2018.2.8
import requests
import sys
sys.path.append('..')
from config import TEST_URL, TOKEN, PROXY_PORT


def client_2_server():
    with requests.post(
        url=TEST_URL,
        data={
            'token': TOKEN,
            'port': PROXY_PORT,
            'name': 'adsl999'
        }
    ) as response:
        if response.status_code == 200:
            print('OK!')


if __name__ == '__main__':
    client_2_server()

