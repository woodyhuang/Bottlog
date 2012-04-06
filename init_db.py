import sqlite3

from utils import execute_sql

execute_sql('drop table if exists blog;')

execute_sql('''
    create table blog
    (id integer primary key,
    title varchar not null,
    content text,
    created_time timestamp,
    last_modified_time timestamp);
''')
