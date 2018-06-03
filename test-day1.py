# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 09:44:58 2018

@author: lenovo
"""

weeks=['星期一','星期二','星期三','星期四','星期五','星期六','星期天']
print(weeks[0])
print(weeks[1])  
print(weeks[2])
print(weeks[3])
print(weeks[4])
print('今天是：'+weeks[5])#今天是星期六
print(weeks[6])


weather={'days':['sat','sun','mon','stu','wen'],
         'climate':[22,24,28,30,31]}
days=weather['days']
print( weather['climate'])
print(max(weather['climate']))


people={'name':'xsj',
 'height':'175',
 'sex':'女',
 'year':'20'}
print(people['name'])
print(people['height'])
print(people['sex'])
print(people['year'])




import urllib.request as r
city_pingyin=input('请输入城市拼音：')

address='http://api.openweathermap.org/data/2.5/weather?q=meishan&mode=json&units=metric&lang=zh_cn&APPID=6a67ed641c0fda8b69715c43518b6996'
info=r.urlopen(address.format(city_pingyin)).read().decode('utf-8','ignore')
print(info)

#json(dict)格式工具包
import json
data=json.loads(info)

print( '城市温度是：'+str(data['main']['temp']),
      '城市气压是：'+str(data['main']['pressure']),
      '城市最低温度是：'+str(data['main']['temp_min']),
      '城市最高温度是：'+str(data['main']['temp_max']))