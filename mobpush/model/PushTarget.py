# -*-coding:utf-8-*-
from mobpush.model.BasePush import BasePush


class PushLabel(BasePush):
    AND = 1
    OR = 2
    NOT = 3

    def __init__(self, labelIds, mobId, type=2):
        self.data = {
            'labelIds': labelIds,
            # 标签列表, 内容是 SmartLabel.id
            # 标签Id不能为空
            'mobId': mobId,
            # mobId不能为空
            'type': type,
            # 标签搭配方式, 1:与, 2:或, 3:非
        }


class PushAreas(BasePush):

    def __init__(self):
        self.data = {
            'countries': [],
            # 需要推送的国家列表
            # message = "地理位置[pushAreas]中国家列表[countries]不能为空"
        }
        """
        单个国家
        {
        "country": str,
        "provinces": {
                "province": str,
                "cities": [str],
                # 如果 cities 不为空，则只推送指定城市
                # 如果 cities 为空，则推送全省
                "excludeCities": [str],
                # 如果 cities 为空，则排除 excludeCities 相关城市的推送
                },
        # 如果 provinces 不为空，则只推送指定省份
        # 如果 provinces 为空，则推送全国
        "excludeProvinces": [str],
        # 如果 provinces 为空，则排除 excludeProvinces 相关省份的推送
        }
        """

    def buildCountry(self, country=None, excludeProvinces=None, provinces=None):
        pushCountry = {
            'country': country,
            'provinces': provinces,
            'excludeProvinces': excludeProvinces,
        }
        result = dict()
        for key in list(pushCountry.keys()):
            if pushCountry.get(key) is not None:
                result[key] = pushCountry.get(key)
        self.data['countries'].append(result)
        return self.data

    def buildProvince(self, province=None, excludeCities=None, cities=None):
        pushProvince = {
            'province': province,
            'cities': cities,
            'excludeCities': excludeCities,
        }
        result = dict()
        for key in list(pushProvince.keys()):
            if pushProvince.get(key) is not None:
                result[key] = pushProvince.get(key)
        return result


class PushTarget(BasePush):
    TARGET_ALL = 1
    TARGET_ALIAS = 2
    TARGET_TAGS = 3
    TARGET_RIDS = 4
    TARGET_AREA = 5
    TARGET_LABEL = 5
    TARGET_SMS = 8
    TARGET_AREAS = 9
    serialVersionUID = 3205738723648870635

    def __init__(self, target=None, tags=None, tagsType=1, alias=None, rids=None, block=None, city=None,
                 country=None, province=None, smartLabels=None, PushAreas=None):
        self.data = {
            'target': target,
            # 推送范围:0 全部；1广播；2别名；3标签；4regid；5地理位置；7智能标签;8短信补量; 9复杂地理位置
            # values = {1, 2, 3, 4, 5, 7,8, 9}, message = "推送消息target错误"
            'tags': tags,
            # target: 3 = > 设置推送标签集合["tag1", "tag2"]
            'tagsType': tagsType,
            # target:3 => 标签组合方式：1并集；2交集；3补集(3暂不考虑)
            'alias': alias,
            # target:2 => 设置推送别名集合["alias1","alias2"]
            'rids': rids,
            # target:4 => 设置推送Registration Id集合["id1","id2"]
            'block': block,
            # target:6 => 用户分群ID
            'city': city,
            'country': country,
            'province': province,
            # target:5 => 推送地理位置
            'smartLabels': smartLabels,
            # target:7 => 智能标签列表, 关联关系为与, 必须同时满足条件
            'PushAreas': PushAreas,
            # target: 8 = > 短信补量
        }
