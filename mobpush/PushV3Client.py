# -*-coding:utf-8-*-
from mobpush.SendRequest import Send
from mobpush.PushWorkBuilder import PushWorkBuilder


class PushV3Client(object):
    baseUrl = "http://api.push.mob.com"
    PUSH_URI = '/v3/push/createPush'
    GET_BY_WORKID_URI = '/v3/push/getByWorkId'
    GET_BY_WORKNO_URI = '/v3/push/getByWorkno'
    CANCEL_TASK_URI = '/push/drop'
    REPLACE_TASK_URI = '/push/replace'
    RECALL_TASK_URI = '/push/recall'

    def __init__(self, app_key, app_secret):
        """
        初始化，传入Appkey和AppSecret
        :param app_key: str
        :param app_secret: str
        """
        self.app_key = app_key
        self.app_secret = app_secret
        self.send = Send(app_key, app_secret)

    def pushTaskV3(self, push):
        """
        用户自定义配置推送
        :param push: dict
        :return: json
        """
        push['Appkey']=self.app_key
        url = self.baseUrl + self.PUSH_URI
        params = push
        result = self.send.get_result(url=url, data=params)
        return result

    def pushAll(self, workNo, title, content):
        """
        广播推送
        :param workNo:
        :param title:
        :param content:
        :return:
        """
        result = self.pushTaskV3(PushWorkBuilder(self.app_key).setTargetAll(workNo=workNo,
                                                                            title=title,
                                                                            content=content))
        return result

    def pushByAlias(self, workNo, title, content, *alias):
        """
        别名推送
        :param workNo:
        :param title:
        :param content:
        :param alias:
        :return:
        """
        alias = list(alias)
        result = self.pushTaskV3(PushWorkBuilder(self.app_key).setTargetByAlias(workNo=workNo,
                                                                                title=title,
                                                                                content=content,
                                                                                alias=alias))
        return result

    def pushByTags(self, workNo, title, content, *tags):
        """
        用户标签推送
        :param workNo:
        :param title:
        :param content:
        :param tags:
        :return:
        """
        tags = list(tags)
        result = self.pushTaskV3(PushWorkBuilder(self.app_key).setTargetTags(workNo=workNo,
                                                                             title=title,
                                                                             content=content,
                                                                             tags=tags))
        return result

    def pushByRids(self, workNo, title, content, *rids):
        """
        Registration ID推送
        :param workNo:
        :param title:
        :param content:
        :param rids:
        :return:
        """
        rids = list(rids)
        result = self.pushTaskV3(PushWorkBuilder(self.app_key).setTargetRids(workNo=workNo,
                                                                             title=title,
                                                                             content=content,
                                                                             rids=rids))
        return result

    def pushByAreas(self, workNo, title, content, pushAreas):
        """
        复杂地理位置推送
        :param workNo:
        :param title:
        :param content:
        :param pushAreas:
        :return:
        """
        result = self.pushTaskV3(PushWorkBuilder(self.app_key).setTargetByAreas(workNo=workNo,
                                                                                title=title,
                                                                                content=content,
                                                                                pushAreas=pushAreas))
        return result

    def getPushByBatchId(self, workId):
        """
        查询推送任务详情
        :param workId:
        :return:
        """
        params = {
            'workId': workId,
        }
        url = self.baseUrl + self.GET_BY_WORKID_URI
        result = self.send.get_result(url=url, data=params)
        return result

    def getPushByWorkno(self, workno):
        """
        查询推送任务详情
        :param workno:
        :return:
        """
        params = {
            'workno': workno,
        }
        url = self.baseUrl + self.GET_BY_WORKNO_URI
        result = self.send.get_result(url=url, data=params)
        return result

    def cancelPushTask(self, workId):
        """
        取消推送任务
        :param workId:
        :return:
        """
        params = {
            'batchId': workId
        }
        url = self.baseUrl + self.CANCEL_TASK_URI
        result = self.send.get_result(url=url, data=params)
        return result

    def replacePushTask(self, batchId, content):
        """
        替换推送任务
        :param batchId:
        :param content:
        :return:
        """
        params = {
            'batchId': batchId,
            'content': content,
        }
        url = self.baseUrl + self.REPLACE_TASK_URI
        result = self.send.get_result(url=url, data=params)
        return result

    def recallPushTask(self, batchId):
        """
        撤回推送任务
        :param batchId:
        :return:
        """
        params = {
            'batchId': batchId,
        }
        url = self.baseUrl + self.RECALL_TASK_URI
        result = self.send.get_result(url=url, data=params)
        return result
