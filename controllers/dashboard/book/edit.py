#controllers/dashboard/book/edit.py
import config
from bottle import template
from copy import deepcopy
from models.bookdb import getdb, editdb

def call(id):
    kdict = deepcopy(config.kdict)
    kdict['siteLogo'] = 'ទំព័រ​សៀវភៅ'
    kdict['route'] = 'book'
    kdict['edit'] = 'edit'

    books, count = getdb.call(kdict['maxItemList'])
    item = editdb.call(id)

    kdict['items'] = books
    kdict['count'] = count
    kdict['item'] = item
    
    return template('dashboard/index.tpl', data=kdict)
