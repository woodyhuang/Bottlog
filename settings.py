import os

DEBUG = True

LOCAL_PATH = os.path.dirname(os.path.abspath(__file__))

DATABASE = os.path.join(LOCAL_PATH, 'myblog.db')

STATIC_ROOT = os.path.join(LOCAL_PATH, 'static')
