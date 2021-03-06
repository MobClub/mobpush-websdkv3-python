# [MobPush API for python](https://www.mob.com/wiki/detailed/?wiki=MobPushRestAPIfenlei1333&id=136)

![image](https://github.com/MOBX/MOB-SMS-WEBAPI/blob/master/doc/images/logo.png)

**[MobPush API for python](https://www.mob.com/wiki/detailed/?wiki=MobPushRestAPIfenlei1333&id=136)** 
为了帮助开发者更方便接入MobPush免费推送SDK，提供完整的API接口的python实现，包含设备操作相关接口、推送操作相关接口以及公共接口。

了解更多 [MobPush 免费推送SDK.](https://www.mob.com/mobService/mobpush)

## 优势

**免费使用**、**自定义UI**、**稳定服务**、**流程体验**、**数据同步**、**专业技术团队服务**

# 接口
## 更新2.0.0版本
* 2.0.0版本新增设备管理和批量推送接口，以及定速推送功能

* 推送接口:
	* 广播推送 pushAll
    * 别名推送 pushByAlias
    * 用户标签推送 pushByTags
    * Registration ID推送 pushByRids
    * 复杂地理位置推送 pushByAreas
    * 用户自定义配置推送 pushTaskV3         
* 推送任务详情查询接口
	* 查询推送任务详情(根据batchId) getPushByBatchId
	* 查询推送任务详情(根据workno) getPushByWorkno
* 推送任务的处理接口
    * 取消推送任务(根据workId) cancelPushTask
    * 替换推送任务(根据workId) replacePushTask
    * 撤回推送任务(根据workId) recallPushTask
* 查询推送统计接口
    * 根据推送任务id查询统计 getStatsByWorkId
    * 根据推送任务id批量查询统计 getStatsByWorkIds
    * 根据用户id查询统计 getStatsByWorkno
    * 按小时查询统计 getStatsByHour
    * 按日期查询统计 getStatsByDay
    * 根据id查询任务下发给设备的详情统计 getStatsByDevice
* 设备操作接口
    * 根据rid查询设备信息接口 getByRid
    * 查询设备分布情况 getDeviceDistribution
    * 根据别名查询设备信息 queryByAlias
    * 更新设备别名 upateByAlias (逐步废弃，请使用updateAlias)
    * 更新设备标签 upateByTags (逐步废弃，updateTags)
    * 根据标签查询设备信息 queryByTags   
       




# 使用方式

* ## pip install mobPushSdkV3
 
# 使用注意事项
* 初始化appkey、appSecret
```python
from mobpush.PushV3Client import PushV3Client
from mobpush.StatsV3Client import StatsV3Client
app_key = 'XXXXXXXXXXXX'
app_secret = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
push_client = PushV3Client(app_key, app_secret)
push_stats = StatsV3Client(app_key, app_secret)
```
以上是使用时设置的方式

* 错误码请参考 
  [MobPush Api 错误码](http://wiki.mob.com/mobpush-rest-api-接口文档/#map-6)



# 使用示例 

发送推送示例片段代码

```python
from mobpush.PushV3Client import PushV3Client
from mobpush.model.PushTarget import PushAreas
app_key = 'XXXXXXXXXXXX'
app_secret = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
push_client = PushV3Client(app_key, app_secret)
workNo = '123456789'
title = 'push title'
content = 'push content'
result = push_client.pushAll(workNo, title, content)
print(result)

country = '中国'
pushAreas = PushAreas()
country = pushAreas.buildCountry(country=country)
result = push_client.pushByAreas(workNo, title, content, pushAreas)
print(result)

excludeProvinces = '湖南'
province = '江苏'
pushAreas = PushAreas()
province = [pushAreas.buildProvince(province=province)]
country = pushAreas.buildCountry(country=country, provinces=province)
result = push_client.pushByAreas(workNo, title, content, pushAreas)
print(result)

cities = ['苏州']
excludeCities = '常州'
pushAreas = PushAreas()
province = [pushAreas.buildProvince(province=province, excludeCities=excludeCities, cities=cities)]
country = pushAreas.buildCountry(country=country, excludeProvinces=excludeProvinces, provinces=province)
result = push_client.pushByAreas(workNo, title, content, pushAreas)
print(result)
```

统计查询示例片段代码

```python
from mobpush.StatsV3Client import StatsV3Client
app_key = 'XXXXXXXXXXXX'
app_secret = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
push_stats = StatsV3Client(app_key, app_secret)
workon = '123456789'
result = push_stats.getStatsByWorkId(workon)
print(result)

