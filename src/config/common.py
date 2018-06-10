# -*- coding:utf-8 -*-

"""
FP-Server main settings
"""

# auto reload
DEBUG = False

# host and ip
HTTP_PORT = 12345

# redirect output to console other than log file
CONSOLE_OUTPUT = 1

# Log
LOG = {
    'level': 'info',
    'dir': '/tmp/logs/fpserver',
    'filename': 'server.log'
}

REDIS = {
    "host": '127.0.0.1',
    "port": 6379,
    "db": 0,
}

# stop crawling new proxies
# after stored enough proxied
PROXY_STORE_NUM = 5000

# Check availability in cycle
PROXY_STORE_CHECK_SEC = 3600
