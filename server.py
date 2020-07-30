# coding: utf-8
# author: QCL
# software: PyCharm Professional Edition 2018.2.8
import time
import tornado.web
import tornado.ioloop
from loguru import logger
from checker.check import main
from application import Application
from multiprocessing import Process
from config import SERVER_PORT, TEST_PROXY_POOL_CYCLE


def test_proxy():
    while True:
        try:
            main()
        except AttributeError:
            time.sleep(TEST_PROXY_POOL_CYCLE)
            continue
        time.sleep(TEST_PROXY_POOL_CYCLE)


def start_server():
    app = Application()
    logger.info(f'Listening on {SERVER_PORT}')
    app.listen(SERVER_PORT)
    tornado.ioloop.IOLoop.instance().start()


def run():
    process_list = []
    server_process = Process(target=start_server)
    process_list.append(server_process)
    server_process.start()

    test_proxy_process = Process(target=test_proxy)
    process_list.append(test_proxy_process)
    test_proxy_process.start()

    for process in process_list:
        process.join()


if __name__ == '__main__':
    run()
