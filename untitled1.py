# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 08:49:17 2018

@author: lenovo
"""

import urllib.request as r
city_pingyin=input('请输入城市拼音：')

address='http://api.openweathermap.org/data/2.5/forecast?q=chengdu,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
info=r.urlopen(address.format(city_pingyin)).read().decode('utf-8','ignore')
print(info)

import json
data=json.loads(info)

day1,day2,day3,day4,day5=0,8,16,24,32
print('欢迎使用全球天气查询系统')
print('当前城市是：成都')
print('时间是：'+str(data['list'][day1]['dt_txt']),
      '城市温度是：'+str(data['list'][day1]['main']['temp']),
      '城市气压是：'+str(data['list'][day1]['main']['pressure']),
      '城市最低温度是：'+str(data['list'][day1]['main']['temp_min']),
      '城市最高温度是：'+str(data['list'][day1]['main']['temp_max']))
print('时间是：'+str(data['list'][day2]['dt_txt']),
      '城市温度是：'+str(data['list'][day2]['main']['temp']),
      '城市气压是：'+str(data['list'][day2]['main']['pressure']),
      '城市最低温度是：'+str(data['list'][day2]['main']['temp_min']),
      '城市最高温度是：'+str(data['list'][day2]['main']['temp_max']))
print('时间是：'+str(data['list'][day3]['dt_txt']),
      '城市温度是：'+str(data['list'][day3]['main']['temp']),
      '城市气压是：'+str(data['list'][day3]['main']['pressure']),
      '城市最低温度是：'+str(data['list'][day3]['main']['temp_min']),
      '城市最高温度是：'+str(data['list'][day3]['main']['temp_max']))
print('时间是：'+str(data['list'][day4]['dt_txt']),
      '城市温度是：'+str(data['list'][day4]['main']['temp']),
      '城市气压是：'+str(data['list'][day4]['main']['pressure']),
      '城市最低温度是：'+str(data['list'][day4]['main']['temp_min']),
      '城市最高温度是：'+str(data['list'][day4]['main']['temp_max']))
print('时间是：'+str(data['list'][day5]['dt_txt']),
      '城市温度是：'+str(data['list'][day5]['main']['temp']),
      '城市气压是：'+str(data['list'][day5]['main']['pressure']),
      '城市最低温度是：'+str(data['list'][day5]['main']['temp_min']),
      '城市最高温度是：'+str(data['list'][day5]['main']['temp_max']))







def printwea(data,day):
    print('时间是：'+str(data['list'][day1]['dt_txt']),
      '城市温度是：'+str(data['list'][day1]['main']['temp']),
      '城市气压是：'+str(data['list'][day1]['main']['pressure']),
      '城市最低温度是：'+str(data['list'][day1]['main']['temp_min']),
      '城市最高温度是：'+str(data['list'][day1]['main']['temp_max']))  










adata=[]
for i in range(38):
    date=data["list"][i]["dt_txt"]
    temp=data["list"][i]["main"]["temp"]
    pressure=data["list"][i]["main"]["pressure"]
    temp_max=data["list"][i]["main"]["temp_max"]
    temp_min=data["list"][i]["main"]["temp_min"]
    predict=("时间是："+str(date),
    "城市温度是："+str(temp),
    "气压是："+str(pressure),
    "最低温度是："+str(temp_min),
    "最高温度是："+str(temp_max))
    adata.append(predict)
print(adata)
print(adata[0],adata[8],adata[16],adata[24],adata[32])


