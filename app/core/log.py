#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: tianzhichao
File: log.py
Time: 2024/10/15 09:28
"""
import os
import sys
import logging
import re
from loguru import logger as lg_logger
from conf.settings import LOG_LEVEL

LOGGER_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))


class InterceptHandler(logging.Handler):
    def emit(self, record):
        logger_opt = logger.opt(depth=6, exception=record.exc_info, colors=False)
        ansi_escape = re.compile(r"\x1B\[[0-?]*[ -/]*[@-~]")
        logger_opt.log(record.levelname, ansi_escape.sub("", record.getMessage()))


def register_logger():
    log_dir = os.path.join(LOGGER_DIR, "log")
    os.makedirs(log_dir, exist_ok=True)

    # 1. 标准日志拦截配置
    logging.basicConfig(handlers=[InterceptHandler(level="INFO")], level="INFO")

    # 2. 控制台输出调整为 JSON 格式
    lg_logger.configure(
        handlers=[{
            "sink": sys.stdout,  # 改为输出到 stdout（容器化部署推荐）
            "level": LOG_LEVEL,
            "serialize": True,  # 关键：输出 JSON 格式
            "format": "{extra[request_id]} | {message}",  # 包含 request_id
            "filter": lambda record: record["extra"].setdefault("request_id", "SYSTEM")
    }]
    )

    # 3. 文件日志保留原有配置，但添加 Loki 所需标签
    # (可选：如果不需要本地文件日志，可注释掉 add() 配置)
    lg_logger.add(
        log_dir + "/info_{time:%Y-%m-%d}.log",
        level="INFO",
        colorize=False,
        rotation="1 days",
        retention="7 days",
        format="{message}",
        serialize=True,
        backtrace=False,
        diagnose=False,
        encoding="utf-8"
    )

    # Error 日志同理...
    lg_logger.add(
        log_dir + "/error_{time:%Y-%m-%d}.log",
        level="ERROR",
        colorize=False,
        rotation="1 days",
        retention="15 days",
        format="{message}",  # 配合 serialize=True 使用
        serialize=True,  # 确保文件日志也是 JSON 格式
        backtrace=False,
        diagnose=False,
        encoding="utf-8"
    )

    return lg_logger


logger = register_logger()
