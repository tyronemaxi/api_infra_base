#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: tianzhichao
File: middleware.py
Time: 2024/10/15 10:10
"""
import os

from flask import Flask, g

from app.engine.pg_cli import session as pg_session
from .auth import auth_handler
from utils.uuid_generator import compress_uuid
from .log import logger

dir_name = os.path.dirname(__file__)


def register_middleware(app: Flask) -> None:
    """
    注册中间件
    """

    @app.before_request
    def auth():
        return None

    @app.teardown_request
    def shutdown_session(exception=None):
        pg_session.remove()

    request_middleware = RequestIDMiddleware(app)


class RequestIDMiddleware:
    def __init__(self, app):
        self.app = app
        self.app.before_request(self._assign_request_id)
        self.app.after_request(self._add_request_id_header)

    @staticmethod
    def _assign_request_id():
        """生成唯一 Request ID 并绑定到日志上下文"""
        request_id = compress_uuid("request")
        g.request_id = request_id  # 存储到 Flask 的全局对象 g
        logger.configure(extra={"request_id": request_id})  # 绑定到 Loguru 上下文

    @staticmethod
    def _add_request_id_header(response):
        """将 Request ID 添加到 HTTP 响应头（可选）"""
        response.headers["X-Request-ID"] = getattr(g, "request_id", "")
        return response
