#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: tianzhichao
File: gunicorn.conf.py.py
Time: 2023/5/3 10:56 PM
"""
from conf.settings import PORT, GUNICORN_ERROR_LOG, GUNICORN_WORKER_NUM

# 1. ip: port -> 绑定端口 注意0.0.0.0的配置在docker网络中是关键配置
bind = f"0.0.0.0:{PORT}"
# 允许pending状态最大连接数 推荐64-2048
backlog = 2048
# 2. 工作进程和并发性能配置 -> worker && worker_class && worker_connections
# 工作进程数 常规使用Docker横向扩容，故按项目实际情况配置
workers = GUNICORN_WORKER_NUM

# 工作单位 除特殊情况外,工程无脑使用gevent 算法可考虑使用gthread
# 详见文档: https://docs.gunicorn.org/en/stable/design.html#choosing-a-worker-type
# 不使用sync的最大问题在于sync虽然在短连接中网络模式最为简单干净,但不支持长连接,在高并发任务中的TCP效率会非常低
worker_class = "gevent"
# 客户端最大同时连接数 在极高并发根据服务器和实例数根据情况修改
# 仅适用于eventlet/gevent
worker_connections = 5000
# 3. 进程管理和重启配置 -> max_requests && max_requests_jitter && timeout && graceful_timeout
# 每执行多少请求,即重启服务 该功能用于防止内存泄漏
# 对算法来说,该功能会导致重新初始化服务 可以设置0为关闭
max_requests = 50000
# 在max_requests 的基础上,随机加减 max_requests_jitter 的参数值 该功能用于防止并发下所有容器同时重启
# 当max_requests=0 时,该配置不生效
max_requests_jitter = 1000
# 超时时间 根据实际情况配置 推荐30/60
timeout = 600
# 是否使用debug模式
debug = 'dev'

# 配置参考：https://docs.gunicorn.org/en/stable/settings.html
# 是否重定向错误到日志文件
capture_output = False
# server 端保持连接时间(秒) 根据情况设置2-5
keepalive = 2
loglevel = 'info'
accesslog = '-'
errorlog = GUNICORN_ERROR_LOG
