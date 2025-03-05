#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: tianzhichao
File: function_call.py
Time: 2024/10/25 14:30
"""

from conf.settings import OPENAI_API_KEY, OPENAI_API_BASE


class FunctionCall(object):
    def get_adcode(self):
        """
        获取城市区代码
        :return:
        """
        pass


    def get_weather(self):
        """
        获取实时天气
        :return:
        """
        pass


tools = FunctionCall()


