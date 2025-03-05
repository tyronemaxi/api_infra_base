#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: tianzhichao
File: __init__.py
Time: 2024/10/15 09:11
"""
from flask import Blueprint, Flask
from flask_restful import Api

from app.routes.infrastructure.healthcheck import HealthCheckResource

# 基础设施路由，用于内部监控，健康检查相关
infra_bp = Blueprint(name="infrastructure", import_name="infrastructure", url_prefix="/infrastructure")
infra = Api(infra_bp)

# 业务功能路由
api_bp = Blueprint(name="api", import_name="api", url_prefix='/api/v1')
api = Api(api_bp)


infra.add_resource(HealthCheckResource, "/healthcheck")


def register_blueprint(app: Flask):
    """
    注册蓝图
    :param app:
    :return:
    """
    app.register_blueprint(infra_bp)
    app.register_blueprint(api_bp)
