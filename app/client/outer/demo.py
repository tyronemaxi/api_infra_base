#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: tianzhichao
File: demo.py
Time: 2024/10/25 16:12
"""
import requests


def get_city_code(city_name, api_key):
    url = f"https://restapi.amap.com/v3/geocode/geo?address={city_name}&key={api_key}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if data['status'] == '1' and len(data['geocodes']) > 0:
            city_code = data['geocodes'][0]['adcode']
            print(f"城市: {data['geocodes'][0]['formatted_address']}, 编码: {city_code}")
        else:
            print("获取城市编码失败:", data.get('info', '未知错误'))
    else:
        print("请求失败:", response.status_code)


if __name__ == "__main__":
    api_key = "f5d278fa2fd1d40b6461a92f183b71b8"

    get_city_code("宜兴", api_key)