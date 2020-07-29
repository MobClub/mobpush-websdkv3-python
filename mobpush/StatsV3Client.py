# -*-coding:utf-8-*-

from mobpush.SendRequest import Send


class StatsV3Client(object):
    baseUrl = 'http://api.push.mob.com'
    GET_BY_WORKID_URI = "/v3/stats/getByWorkId"
    GET_BY_WORKIDS_URI = "/v3/stats/getByWorkIds"
    GET_BY_WORKNO_URI = "/v3/stats/getByWorkno"
    GET_BY_HOUR_URI = "/v3/stats/getByHour"
    GET_BY_DAY_URI = "/v3/stats/getByDay"
    GET_BY_DEVICE_URI = "/v3/stats/getByDevice"

    def __init__(self, app_key, app_secret):
        if app_key:
            self.app_key = app_key
            self.app_secret = app_secret
            self.send = Send(app_key, app_secret)

    def getStatsByWorkId(self, work_id):
        """
        根据推送任务id查询统计
        :param work_id: 任务Id
        :return: dict
        """
        params = {
            'workId': work_id,
        }

        url = self.baseUrl + self.GET_BY_WORKID_URI
        result = self.send.get_result(url=url, data=params)
        return result

    def getStatsByWorkIds(self, *work_id_list):
        """
        根据推送任务id批量查询统计
        :param work_id_list:[任务Id, 任务Id, 任务Id]
        :return: dict
        """
        params = {
            'workIds': list(work_id_list),
        }
        url = self.baseUrl + self.GET_BY_WORKIDS_URI
        result = self.send.get_result(url=url, data=params)
        return result

    def getStatsByWorkno(self, work_no: str):
        """
        根据用户的id查询统计
        :param work_no: 用户的推送任务id
        :return: dict
        """
        params = {
            'workno': work_no,
        }
        url = self.baseUrl + self.GET_BY_WORKNO_URI
        result = self.send.get_result(url=url, data=params)
        return result

    def getStatsByHour(self, hour):
        """
        按小时查询统计
        :param hour: 时间精确到小时  示例：2020102615
        :return: dict
        """
        params = {
            'hour': hour,
        }
        url = self.baseUrl + self.GET_BY_HOUR_URI
        result = self.send.get_result(url=url, data=params)
        return result

    def getStatsByDay(self, day):
        params = {
            'day': day,
        }
        url = self.baseUrl + self.GET_BY_DAY_URI
        result = self.send.get_result(url=url, data=params)
        return result

    def getStatsByDevice(self, work_id, page_index, page_size):
        """
        统计每次下发的设备信息
        :param work_id: 任务id
        :param page_index: 页码
        :param page_size: 每页数量
        :return: dict
        """
        params = {
            'workId': work_id,
            'pageIndex': page_index,
            'pageSize': page_size,
        }
        url = self.baseUrl + self.GET_BY_DEVICE_URI
        result = self.send.get_result(url=url, data=params)
        return result
