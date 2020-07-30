# coding: utf-8
# author: QCL
# software: PyCharm Professional Edition 2018.2.8
import asyncio
import aiohttp
from loguru import logger
from urllib.parse import urlencode
from storages.redisclient import RedisClient

import sys
sys.path.append('..')
from config import TEST_URL


def get_proxies():
    logger.info('Get Proxies')
    proxy_dict = RedisClient().all()
    if proxy_dict:
        return proxy_dict
    else:
        logger.info('Proxies Empty!')


async def test_proxy(item, session):
    name, proxy = item
    logger.info(f'Testing Proxy, {name}, {proxy}')
    test_url = TEST_URL + '?' + urlencode({'name': name})
    try:
        async with session.get(
            url=test_url,
            proxy='http://' + proxy,
            headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                              'Chrome/83.0.4103.97 Safari/537.36'
            }
        ) as response:
            if response.status == 200:
                logger.info(f'Valid Proxy, {name}')
    except Exception as e:
        logger.error(e)
        logger.info(f'InValid Proxy, {name}')
        res = RedisClient().remove(name)
        if res:
            logger.info(f'Remove Proxy From Redis Successfully, {name}')


async def run():
    async with aiohttp.TCPConnector(ssl=False) as tc:
        async with aiohttp.ClientSession(connector=tc) as session:
            tasks = []
            try:
                for item in get_proxies().items():
                    tasks.append(asyncio.ensure_future(test_proxy(item, session)))
                await asyncio.wait(tasks)
            except AttributeError:
                raise AttributeError


def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())


if __name__ == '__main__':
    main()
