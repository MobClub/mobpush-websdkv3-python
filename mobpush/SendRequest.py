# -*-coding:utf-8-*-
import hashlib
import json

import requests

class ApiException(BaseException):
    pass


class Send(object):
    app_key = None
    app_secret = None

    def __init__(self, app_key: str, app_secret: str):
        self.app_key = app_key  # 需要先设置此数据，怎样获取appkey请至http://www.mob.com官网
        self.app_secret = app_secret  # appkey对应密钥,需要先设置此数据

    def get_result(self, url:str, data:dict, headers=None):
        """
        发送请求
        :param url: 要请求的url
        :param data: 请求参数
        :param headers: 请求头
        :return: dict
        """
        if not data.get('appKey', None):
            data['appKey'] = self.app_key
        data = json.dumps(data)
        if not headers:
            headers = self.make_headers(data)
        response = requests.post(url=url,
                                 data=data,
                                 headers=headers,
                                 timeout=10
                                 )
        if response.status_code == 500:
            raise ApiException(response.text)
        res = response.json()
        if response.status_code != 200:
            res['status_code'] = response.status_code
        return res

    def make_headers(self, data:str):
        """
        生成默认请求头
        :param data: json化请求参数
        :return: headers
        """
        headers = dict()
        m = hashlib.md5()
        m.update(bytes(data+self.app_secret, encoding='utf-8'))
        headers['sign'] = m.hexdigest()
        headers['key'] = self.app_key
        return headers