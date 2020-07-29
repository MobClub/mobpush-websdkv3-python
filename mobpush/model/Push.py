# -*-coding:utf-8-*-
from mobpush.model.BasePush import BasePush
from mobpush.model.PushNotify import PushNotify
from mobpush.model.PushOperator import PushOperator


class Push(BasePush):
    TASK_CRON_ENABLE = 1
    BUSINESS_TYPE_AD = 1
    IOS_PROD = 1
    IOS_DEV = 0
    serialVersionUID = -1914482721382496441

    def __init__(self, appKey, workno=None, source='webapi', pushFroward=None):
        self.data = {
            'workno': workno,
            # 推送任务标识，对接用户服务端唯一ID，传入后原样返回（用户服务端自有）
            'source': source,
            # 推送任务来源：webapi 、developerPlatform
            # values = {"webapi", "upsapi", "sdkapi", "devplat"}, message = "消息源格式错误"
            'appKey': appKey,
            'pushTarget': None,
            'pushNotify': PushNotify().get_result(),
            # 推送展示细节
            'pushOperator': PushOperator().get_result(),
            # 运营保障相关配置
            'pushFroward': pushFroward,
            # link 相关打开配置
        }
