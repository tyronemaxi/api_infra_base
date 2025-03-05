#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: tyrone
File: tools.py
Time: 2024/11/3
"""
import json

from openai import OpenAI

from app.client.outer.weather import weather_cli, city_codes_cli
from conf.settings import OPENAI_API_KEY, OPENAI_API_BASE
from app.core.log import logger


def get_city_code(query: str):
    """
    获取城市 acode
    """
    city_code = city_codes_cli.get_adcode(query)

    return city_code


def parse_weather_response(response):

    if response['status'] != '1':
        return "无法获取天气信息"

    forecasts = response['forecasts'][0]  # 获取第一个城市的天气预报
    city = forecasts['city']
    province = forecasts['province']
    report_time = forecasts['reporttime']

    weather_info = [f"{city}, {province} 天气预报（数据更新时间：{report_time}）:\n"]

    for cast in forecasts['casts']:
        date = cast['date']
        week = cast['week']
        day_weather = cast['dayweather']
        night_weather = cast['nightweather']
        day_temp = cast['daytemp']
        night_temp = cast['nighttemp']
        day_wind = cast['daywind']
        night_wind = cast['nightwind']

        weather_info.append(
            f"{date}（周{week}）: "
            f"白天气温 {day_temp}°C，天气：{day_weather}，风向：{day_wind}; "
            f"夜间气温 {night_temp}°C，天气：{night_weather}，风向：{night_wind}\n"
        )

    return ''.join(weather_info)


def get_weather(acode: str):
    """
    获取天气
    """
    resp = weather_cli.get_weather(acode)
    data = parse_weather_response(resp)
    logger.info(f"天气情况: {data}")
    return data


tools = [
    {
        "type": "function",
        "function": {
            "name": "get_city_code",
            "description": "根据用户的问题，获取城市名",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "用户问题"
                    }
                },
                "required": ["query"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "根据城市编码，获取实时天气情况",
            "parameters": {
                "type": "object",
                "properties": {
                    "acode": {
                        "type": "string",
                        "description": "城市 acode"
                    }
                },
                "required": ["acode"]
            }
        }
    },
]


def get_completion(messages, model):
    client = OpenAI(base_url=OPENAI_API_BASE,
                    api_key=OPENAI_API_KEY)

    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0,
        max_tokens=1024,
        tools=tools
    )

    return response.choices[0].message


def chat(prompt, model='gpt-4'):
    messages = [
        {"role": "system", "content": "你是一个天气查询助手"},
        {"role": "user", "content": prompt}
    ]

    resp = get_completion(messages, model)
    messages.append(resp)

    while resp.tool_calls:
        for tool in resp.tool_calls:
            args = json.loads(tool.function.arguments)
            print("参数", args)

            if tool.function.name == "get_city_code":
                result = get_city_code(**args)
                logger.info(f"{result}")

            elif tool.function.name == "get_weather":
                result = get_weather(**args)
                logger.info(f"{result}")

            messages.append(
                {
                    "tool_call_id": tool.id,
                    "role": "tool",
                    "name": tool.function.name,
                    "content": result,
                }
            )  # extend conversation with function response

            resp = get_completion(messages, model)
            messages.append(resp)

    # resp = get_completion(messages, model)
    print(resp.content)


if __name__ == '__main__':
    prompt = "苏州今天天气如何？"
    chat(prompt)
    # resp = get_city_code("今天天气怎么样")
    # print(resp)
