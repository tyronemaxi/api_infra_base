#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: tianzhichao
File: server.py
Time: 2024/10/15 09:09
"""
from flask import Flask

from app.core.log import register_logger
from app.routes import register_blueprint
from app.extension import register_extension

from app.core.errors import register_error_handler
from app.core.middleware import register_middleware
from app.core.flask_config import Configs
from app.core.json_encoder import CustomJSONEncoder

from conf.settings import ENV
from conf.settings import PORT


def create_app():
    app = Flask(__name__)
    app.json_provider_class = CustomJSONEncoder
    app.config.from_object(Configs[ENV])

    register_logger()
    register_blueprint(app)

    register_extension(app)
    register_error_handler(app)
    register_middleware(app)

    # [保留flask本身错误处理]
    handle_exceptions = app.handle_exception
    handle_user_exception = app.handle_user_exception

    # [覆盖flask-restful的error handler为flask原生error handler]
    app.handle_exception = handle_exceptions
    app.handle_user_exception = handle_user_exception

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(port=PORT, host='0.0.0.0', use_reloader=True, debug=True)
