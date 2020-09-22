# -*-coding:utf-8-*-
from mobpush.model.BasePush import BasePush


class IosNotify(BasePush):
    serialVersionUID = 6316980682876425791
    BADGE_TYPE_SET = 1
    BADGE_TYPE_ADD = 2
    SLIENT = 1

    def __init__(self, title=None, subtitle=None, attachment=None,
                 attachmentType=None, mutableContent=None, contentAvailable=None,
                 slientPush=None, category=None, badgeType=None, badge=None, sound='default'):
        self.data = {
            'title': title,
            # 标题- 不填写则为应用名称
            'subtitle': subtitle,
            # 副标题
            'sound': sound,
            # APNs通知，通过这个字段指定声音。默认为default，即系统默认声音。 如果设置为空值，则为静音。
            # 如果设置为特殊的名称，则需要你的App里配置了该声音才可以正常。
            'badge': badge,
            # 可直接指定 APNs 推送通知的 badge，未设置这个值角标则不带角标推送
            'badgeType': badgeType,
            # badgeAdd=true 时，增加badge对应的角标数，负数时，算减法
            # 当这个数值设置了值时，会更新数据库数据
            # 未设置这个值角标则不带角标推送
            # 1: 绝对值，2: 修改值
            'category': category,
            # 只有IOS8及以上系统才支持此参数推送
            'slientPush': slientPush,
            # 如果只携带content-available: 1,不携带任何badge，sound 和消息内容等参数，
            # 则可以不打扰用户的情况下进行内容更新等操作即为“Silent Remote Notifications”。
            'contentAvailable': contentAvailable,
            # 将该键设为 1 则表示有新的可用内容。带上这个键值，意味着你的 App 在后台启动了或恢复运行了，application:didReceiveRemoteNotification:fetchCompletionHandler:被调用了。
            'mutableContent': mutableContent,
            # 需要在附加字段中配置相应参数
            'attachmentType': attachmentType,
            # ios富文本0无 ；1 图片 ；2 视频 ；3 音频

            'attachment': attachment,
        }


class AndroidNotify(BasePush):
    def __init__(self, appName=None, title=None, sound=None, warn='12', style=0, content=None):
        self.data = {
            'appName': appName,
            # 通知标题
            'title': title,
            # 如果不设置，则默认的通知标题为应用的名称。
            # max = 20, message = "推送标题最大长度20"
            'warn': warn,
            # warn:  提醒类型： 1提示音；2震动；3指示灯
            # 如果多个组合则对应编号组合如：12 标识提示音+震动
            'style': style,
            # 显示样式标识  0、默认通知无； 1、长内容则为内容数据； 2、大图则为图片地址； 3、横幅则为多行内容
            # values = {0, 1, 2, 3}, message = "安卓消息格式参数错误"
            'content': content,
            # content:  style样式具体内容
            'sound': sound,
            # 自定义声音
        }


class CustomNotify(BasePush):
    def __init__(self, customType=None, customTitle=None):
        self.data = {
            'customType': customType,
            # 自定义消息类型：text 文本消息
            'customTitle': customTitle
            # 自定义类型标题
        }


class PushNotify(BasePush):
    def __init__(self, taskCron=0, taskTime=None, plats=[1, 2], iosProduction=1, offlineSeconds=3600,
                 content=None, title=None, type=1, customNotify=None, androidNotify=None, iosNotify=None,
                 url=None, extrasMapList=[]):
        self.data = {
            'taskCron': taskCron,
            # 是否是定时任务：0否，1是，默认0
            'taskTime': taskTime,
            # 定时消息 发送时间
            'speed': 0,
            # 定速推送, 设置平均每秒推送速度
            # 0: 不限制
            # 其他限制速度
            # 例如: 每秒1条,每秒100条, 建议最小设置为100条
            # 这个只是模糊的控制, 只保证推送整体上的平均数值, 比如设置为1, 每5秒推送一条
            'plats': plats,
            # 可使用平台，1 android;2 ios ;3 winphone(暂不使用) ;
            'iosProduction': iosProduction,
            # plat = 2下，0测试环境，1生产环境，默认1
            'offlineSeconds': offlineSeconds,
            # 离线时间，秒
            'content': content,
            # 推送内容
            'title': title,
            # 推送标题
            'type': type,
            # 推送类型：1通知；2自定义
            # values = {1, 2}, message = "消息类型1：通知，2：自定义"
            'customNotify': customNotify,
            # 自定义内容, type=2
            'androidNotify': androidNotify,
            # android通知消息, type=1, android
            'iosNotify': iosNotify,
            # ios通知消息, type=1, ios
            'url': url,
            # 打开链接
            'extrasMapList': extrasMapList,
            # 附加字段键值对的方式
        }
