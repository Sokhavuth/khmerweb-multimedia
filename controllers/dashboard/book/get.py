#controllers/dashboard/book/get.py
import config
from bottle import template
from copy import deepcopy
from models.bookdb import getdb

def call():
    kdict = deepcopy(config.kdict)
    kdict['siteLogo'] = 'ទំព័រ​សៀវភៅ'
    kdict['route'] = 'book'

    books, count = getdb.call(kdict['maxItemList'])
    kdict['items'] = books
    kdict['count'] = count

    return template('dashboard/index.tpl', data=kdict)