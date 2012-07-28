import sqlite3
import logging

import creole
from  creole.html_emitter import HtmlEmitter

from bottle import HTTPError

import settings


def init_logger(log_file='bottlog.log', level=logging.DEBUG):
    logger = logging.getLogger('bottlog_logger')
    logger.setLevel(level)

    from logging import handlers
    fhandler = handlers.RotatingFileHandler(
                                        log_file,
                                        backupCount=5, 
                                        maxBytes=1024*1024*50, #50MB
                                        mode='a')  
    fhandler.setLevel(level)

    formatter = logging.Formatter('%(asctime)s %(levelname)s [%(module)s:%(lineno)d] %(message)s')

    fhandler.setFormatter(formatter)
    logger.addHandler(fhandler)
    
    if settings.DEBUG:
        shandler = logging.StreamHandler()
        shandler.setLevel(level)
        shandler.setFormatter(formatter)
        logger.addHandler(shandler)

    return logger

LOG = init_logger() if settings.DEBUG else init_logger(level=logging.INFO)


def execute_sql(sql, args=None):
    '''
    Return a list as result.
    '''
    result = None
    
    LOG.debug('sql is : %s' , sql)

    con = sqlite3.connect(settings.DATABASE)
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    try:
        with con:
            if args:
                cur.execute(sql, args)
            else:
                cur.execute(sql)
            # you need to fetchone even if you have given the unique condition
            result = cur.fetchall()
    except Exception, e:
        LOG.critical('error when executing sql: %s', sql)
        LOG.critical(e)
        raise HTTPError(500, 'Database error.')
    finally:
        cur.close()
        con.close()
    return result


def wiki2html(wiki_str):
    return HtmlEmitter(creole.Parser(wiki_str).parse()).emit()

MON_NAME = {'01': 'JAN',
            '02': 'FEB',
            '03': 'MAR',
            '04': 'APR',
            '05': 'MAY',
            '06': 'JUNE',
            '07': 'JULY',
            '08': 'AUG',
            '09': 'SEPT',
            '10': 'OCT',
            '11': 'NOV',
            '12': 'DEC',}
def get_month_name(date_str):
    '''
    date_str looks like: 2012-04-06 13:29:11.820000
    '''
    return MON_NAME.get(date_str.split('-', 2)[1])

def get_day(date_str):
    return date_str.split('-', 2)[2][:2]
