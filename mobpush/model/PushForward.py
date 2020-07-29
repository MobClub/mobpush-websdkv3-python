# -*-coding:utf-8-*-
from mobpush.model.BasePush import BasePush


class PushForward(BasePush):
    def __init__(self, nextType=1, url=None, scheme=None, schemeDataList=[]):
        self.data={
            'nextType': nextType,
            # 0 打开首页 1 url跳转 2  scheme 跳转
            'url': url,
            # 跳转
            'scheme': scheme,
            # scheme功能的的uri
            'schemeDataList': schemeDataList,
            # moblink功能的参数 a=123&b=345
        }
