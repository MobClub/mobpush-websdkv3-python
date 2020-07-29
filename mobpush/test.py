# -*-coding:utf-8-*-
from mobpush.PushV3Client import PushV3Client
from mobpush.StatsV3Client import StatsV3Client
from mobpush.model.PushTarget import PushAreas

app_key = '2dbe655e88c80'
app_secret = 'a7b9f1918c596eacbff8a172ba8ed158'
push_client = PushV3Client(app_key, app_secret)
push_client.baseUrl = 'http://10.18.97.47:8082'

workNo=''
title='tianzong'
content='tianzong'

# test_pushAll
result = push_client.pushAll(None, 'push title', 'push content')
print(result)
result = push_client.pushAll('123456789', None, 'push content')
print(result)
result = push_client.pushAll('12312345', 'push title', 'push content')
print(result)
result = push_client.pushAll('12312345', 'push title', 'push content')
print(result)
result = push_client.pushAll(None, 'push title', None)
print(result)


# test_push_by_alias
ailas1 = '1111'
ailas2 = '2222'
ailas3 = '3333'
result = push_client.pushByAlias(workNo, title, content, ailas1)
print(result)
result = push_client.pushByAlias(workNo, title, content, ailas1, ailas2, ailas3)
print(result)
result = push_client.pushByAlias(workNo, title, content)
print(result)


# test_push_by_tags
tag1 = 'tianzong'
tag2 = 'tianzong2'
tag3 = 'tianzong3'
result = push_client.pushByTags(workNo, title, content, tag1)
print(result)
result = push_client.pushByTags(workNo, title, content, tag1, tag2, tag3)
print(result)
result = push_client.pushByTags(workNo, title, content)
print(result)


# test_push_by_rids
rid1 = '65oub3zcm169s00'
rid2 = '65oub3zcm169s11'
rid3 = '65oub3zcm169s22'
result = push_client.pushByRids(workNo, title, content, rid1)
print(result)
result = push_client.pushByRids(workNo, title, content, rid1, rid2, rid3)
print(result)
result = push_client.pushByRids(workNo, title, content)
print(result)


# test_push_by_areas
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

# test_batchId
result = push_client.pushAll('', 'push title', 'push content')
batchId = result.get('res').get('batchId')

result = push_client.getPushByBatchId(batchId)
print(result)

content = '替换呀'
result = push_client.replacePushTask(batchId, content)
print(result)

result = push_client.recallPushTask(batchId)
print(result)

result = push_client.cancelPushTask(batchId)
print(result)

workno="123abc"
result = push_client.getPushByWorkno(workno)
print(result)


stats = StatsV3Client(app_key, app_secret)
stats.baseUrl = 'http://10.18.97.47:8082'

workno1 = '123abc'
workno2 = '123123'
workno3 = '123456'

result = stats.getStatsByWorkId(workno1)
print(result)

result = stats.getStatsByWorkIds(workno1, workno2, workno3)
print(result)

result = stats.getStatsByWorkno(workno1)
print(result)

result = stats.getStatsByHour('2020072615')
print(result)

result = stats.getStatsByDay('20200715')
print(result)

result = stats.getStatsByDevice(batchId, 1, 20)
print(result)