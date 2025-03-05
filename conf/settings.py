#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: tianzhichao
File: settings.py
Time: 2024/10/15 09:48
"""
import os
import pytz

from dotenv import load_dotenv

PROJECT_DIR = os.path.dirname(os.path.dirname(__file__))

# [base]
ENV = os.getenv("ENV", 'dev')
TZ = pytz.timezone(os.getenv("TZ", "Asia/Shanghai"))

# [读取.env文件，转化为环境变量]
load_dotenv(os.path.join(PROJECT_DIR, f".env.{ENV}"))
PORT = int(os.getenv("PORT", 8080))
LOG_LEVEL = os.getenv("LOG_LEVEL", "DEBUG")
GUNICORN_ERROR_LOG = os.getenv("GUNICORN_ERROR_LOG", "-")
SECRET_KEY = os.getenv("SECRET_KEY")
GUNICORN_WORKER_NUM = int(os.getenv("GUNICORN_WORKER_NUM", 2))

# [DB]
DB_HOST = os.getenv("DB_HOST", "127.0.0.1")
DB_DATABASE = os.getenv("DB_DATABASE", "postgres")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_USER = os.getenv("DB_USER", "pgembedding")
DB_PASSWORD = os.getenv("DB_PASSWORD", "QWed34|lujf")
SQL_PRINT = False if os.getenv("SQL_PRINT") == "False" else True
POOL_RECYCLE = int(os.getenv("POOL_RECYCLE", 300))
POOL_SIZE = int(os.getenv("POOL_SIZE", 10))
MAX_OVERFLOW = int(os.getenv("MAX_OVERFLOW", 10))
POOL_TIMEOUT = int(os.getenv("POOL_TIMEOUT", 30))

# [REDIS]
REDIS_HOST = os.getenv("REDIS_HOST")
REDIS_PORT = os.getenv("REDIS_PORT")
REDIS_PASSWORD = os.getenv("REDIS_PASSWORD")
REDIS_CACHE_DB = os.getenv("REDIS_CACHE_DB")
CELERY_BROKER_DB = os.getenv("CELERY_BROKER_DB")

# [Minio]
MINIO_IP = os.getenv("MINIO_IP")
MINIO_AK = os.getenv("MINIO_AK")
MINIO_SK = os.getenv("MINIO_SK")

# [数据目录]
DATA_DIR = os.path.join(PROJECT_DIR, "data")

# [JWT]
ENABLE_QW_LOGIN = True if os.getenv("ENABLE_QW_LOGIN") == "True" else False
JWT_AUTH_VERSION = os.getenv("JWT_AUTH_VERSION")

# [openai]
OPENAI_API_BASE = os.getenv("OPENAI_API_BASE")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
