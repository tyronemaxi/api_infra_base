#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: tianzhichao
File: weather.py
Time: 2024/10/25 15:24
"""
from app.client.base import BaseRequests

api_key = "f5d278fa2fd1d40b6461a92f183b71b8"


class Weather(BaseRequests):
    def get_weather(self, city: str):
        """
        获取制定城市的天气信息
        :param city: 城市名
        :return:
        """
        params = {
            "key": api_key,
            "city": city,
            "extensions": "all",
            "output": "JSON",
        }

        resp = self.get(params=params)
        return resp.json()


class CityCodes(BaseRequests):
    def get_adcode(self, city: str):
        """
        获取城市的adcode
        :param city:
        :return:
        """
        params = {
            "address": city,
            "key": api_key,
        }
        resp = self.get(params=params)
        print(resp.json())

        if resp.status_code == 200:
            code = resp.json()['geocodes'][0]['adcode']
        else:
            raise Exception(f"获取城市编码失败, {city}")

        return code


weather_cli = Weather(base_url="https://restapi.amap.com/v3/weather/weatherInfo", is_retry=True)
city_codes_cli = CityCodes(base_url="https://restapi.amap.com/v3/geocode/geo", is_retry=True)


if __name__ == '__main__':
    city_code = city_codes_cli.get_adcode("苏州吴中")
    resp = weather_cli.get_weather(city_code)
    print(resp)
