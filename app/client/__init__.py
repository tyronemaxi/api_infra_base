#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: tianzhichao
File: __init__.py
Time: 2024/10/16 09:38
"""
from .outer.weather import weather_cli, city_codes_cli

__all__ = [
    "weather_cli",
    "city_codes_cli"
]