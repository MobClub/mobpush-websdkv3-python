# -*-coding:utf-8-*-
from mobpush.model.Push import Push
from mobpush.model.PushTarget import PushTarget


class PushWorkBuilder(object):
    TARGET_ALL = 1
    TARGET_ALIAS = 2
    TARGET_TAGS = 3
    TARGET_RIDS = 4
    TARGET_AREAS = 9

    def __init__(self, appKey):
        self.push = Push(appKey).get_result()

    def build(self):
        return self.push

    def fillParams(self, workNo, title, content):
        if not self.push.get('PushTarget'):
            push_target = PushTarget()
            self.push['PushTarget'] = push_target.get_result()
        self.push['workno'] = workNo
        self.push['pushNotify']['title'] = title
        self.push['pushNotify']['content'] = content

    def setTargetAll(self, workNo, title, content):
        self.fillParams(workNo=workNo, title=title, content=content)
        self.push['PushTarget']['target'] = self.TARGET_ALL
        return self.push

    def setTargetByAlias(self, workNo, title, content, alias):
        self.fillParams(workNo=workNo, title=title, content=content)
        self.push['PushTarget']['target'] = self.TARGET_ALIAS
        self.push['PushTarget']['alias'] = list(alias)
        return self.push

    def setTargetTags(self, workNo, title, content, tags):
        self.fillParams(workNo=workNo, title=title, content=content)
        self.push['PushTarget']['target'] = self.TARGET_TAGS
        self.push['PushTarget']['tags'] = list(tags)
        return self.push

    def setTargetRids(self, workNo, title, content, rids):
        self.fillParams(workNo=workNo, title=title, content=content)
        self.push['PushTarget']['target'] = self.TARGET_RIDS
        self.push['PushTarget']['rids'] = list(rids)
        return self.push

    def setTargetByAreas(self, workNo, title, content, pushAreas):
        self.fillParams(workNo=workNo, title=title, content=content)
        self.push['PushTarget']['target'] = self.TARGET_AREAS
        self.push['PushTarget']['pushAreas'] = pushAreas.get_result()
        return self.push

    def setNotifyExtraParams(self, key, value):
        push_map = {
            'key': key,
            'value': value
        }
        self.push['pushNotify']['extrasMapList'].append(push_map)
        return self.push

    def setNotifyExtraMap(self, extra_map):
        self.push['pushNotify']['extrasMapList'] = self.getExtraParamsList(extra_map)
        return self.push

    def setForwardExtraParams(self, key, value):
        push_map = {
            'key': key,
            'value': value
        }
        self.push['pushNotify']['schemeDataList'].append(push_map)
        return self.push

    def setForwardExtraMap(self, extra_map):
        self.push['pushNotify']['schemeDataList'] = self.getExtraParamsList(extra_map)
        return self.push

    def getExtraParamsList(self, extra_map):
        push_map_list = []
        for k, v in extra_map.items():
            push_map_list.append({
                'key': str(k),
                'value': str(extra_map.get(k))
            })
        return push_map_list

