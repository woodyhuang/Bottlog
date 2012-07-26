import os

DEBUG = True

LOCAL_PATH = os.path.normpath(os.path.dirname(os.path.abspath(__file__)))

DATABASE = os.path.normpath(os.path.join(LOCAL_PATH, 'myblog.db'))

STATIC_ROOT = os.path.normpath(os.path.join(LOCAL_PATH, 'static'))
