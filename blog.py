# -*- coding: utf-8 -*-
from datetime import datetime

from bottle import Bottle, view, request, redirect, static_file, HTTPError
myapp = Bottle()

import settings
from utils import execute_sql, LOG

from bottle_i18n import I18NPlugin
i18n = I18NPlugin(domain='myblog')
myapp.install(i18n)

@myapp.get('/')
@view('index')
def index():
    blogs = execute_sql('select id, title, created_time, content from blog')
    return {'blogs':blogs}


@myapp.get('/post')
@view('post_form')
def post_form():
    return {}


@myapp.post('/post')
def do_post():
    title = request.forms.title
    content = request.forms.content
    created_time = datetime.now()
    modified_time = created_time
    
    execute_sql('insert into blog values (?,?,?,?,?)' ,
                    (None, title, content, created_time, modified_time))

    redirect('/')

@myapp.get('/post/<id>')
@view('detail')
def detail(id):
    blogs = execute_sql('select id, title, created_time, content from blog where id =?', (id,))
    if not len(blogs):
        raise HTTPError(404, 'Blog does not exist.')
    LOG.debug('column created time type: %s', type(blogs[0]['created_time']))
    #myapp.set_lang(['jp'])
    msg = myapp._('test i18n in py')
    LOG.debug('i18n msg: %s', msg)
    myapp.set_lang(['ja'])
    return {'blog': blogs[0], 'msg':msg, '_': myapp._}


#@myapp.error(404)
#def error404(error):
#    return 'Nothing here, sorry'


@myapp.route('/static/<filename:path>')
def serve_static(filename):
    return static_file(filename, root=settings.STATIC_ROOT)
