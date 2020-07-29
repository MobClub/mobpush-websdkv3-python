# -*-coding:utf-8-*-


class BasePush(object):
    data = dict()

    def get_result(self):
        result = dict()
        for key in list(self.data.keys()):
            if self.data.get(key) is not None:
                result[key] = self.data.get(key)
        return result
