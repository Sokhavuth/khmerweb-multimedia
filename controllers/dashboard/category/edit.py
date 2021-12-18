#controllers/dashboard/category/edit.py
import config
from bottle import template
from copy import deepcopy
from models.categorydb import getdb, editdb

def call(id):
    kdict = deepcopy(config.kdict)
    kdict['siteLogo'] = 'ទំព័រ​ជំពូក'
    kdict['route'] = 'category'
    kdict['edit'] = 'edit'

    categories, count = getdb.call(kdict['maxItemList'])
    item = editdb.call(id)

    kdict['items'] = categories
    kdict['count'] = count
    kdict['item'] = item
    
    return template('dashboard/index.tpl', data=kdict)
