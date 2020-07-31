# coding: utf-8
# author: QCL
# software: PyCharm Professional Edition 2018.2.8
from loguru import logger
from tornado.web import RequestHandler
from tornado.httpclient import HTTPRequest
from storages.redisclient import RedisClient
from urllib.parse import urlencode, parse_qs, urlsplit
from tornado.curl_httpclient import CurlAsyncHTTPClient

import sys
sys.path.append('..')
from config import TEST_URL, TOKEN, CLIENT_NAME


class MainHandler(RequestHandler):

    redis = RedisClient()
    http_client = CurlAsyncHTTPClient(force_instance=True)

    def handle_proxy(self, response):
        request = response.request
        host = request.proxy_host
        port = request.proxy_port
        name = parse_qs(urlsplit(request.url).query).get('name')[0]
        proxy = '{host}:{port}'.format(host=host, port=port)
        if response.error:
            logger.error(f'Request failed Using, {proxy}, {response.error}')
            logger.error(f'Invalid Proxy, {proxy}, Remove it')
            self.redis.remove(name)
        else:
            logger.info(f'Valid Proxy, {name}')

    def get_proxies(self):
        logger.info('Get Proxies')
        proxy_dict = self.redis.all()
        if proxy_dict:
            for item in proxy_dict.items():
                yield item

    def test_proxy(self):
        for item in self.get_proxies():
            name, proxy = item
            try:
                proxy_host, proxy_port = tuple(proxy.split(':'))
                logger.info(f'Testing Proxy, {name}, {proxy}')
                test_url = TEST_URL + '?' + urlencode({'name': name})
                request = HTTPRequest(url=test_url, proxy_host=proxy_host, proxy_port=int(proxy_port))
                self.http_client.fetch(request, self.handle_proxy)
            except ValueError:
                logger.error(f'Invalid Proxy, {proxy}')

    def post(self):
        token = self.get_body_argument('token', default=None, strip=False)
        port = self.get_body_argument('port', default=None, strip=False)
        name = self.get_body_argument('name', default=None, strip=False)
        if token == TOKEN and port:
            ip = self.request.remote_ip
            proxy = ip + ':' + port
            logger.info(f'Receive proxy, {proxy}')
            try:
                res = self.redis.set(name, proxy)
                if res:
                    # self.test_proxy()
                    logger.info(f'Saving proxy To Redis Successfully, {proxy}')
            except Exception as e:
                logger.error(e.args)
        elif token != TOKEN:
            self.write('Wrong Token')
        elif not port:
            self.write('No Client Port')

    def get(self, api):
        if api == CLIENT_NAME:
            res = self.redis.remove(CLIENT_NAME)
            if res:
                self.write('Removing Proxy Successfully')
        if api == 'random':
            result = self.redis.random()
            if result:
                self.write(result)

        if api == 'counts':
            self.write(str(self.redis.count()))





