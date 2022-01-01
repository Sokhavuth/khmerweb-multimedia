#controllers/backend/categories/edit.py
import config
from bottle import template
from copy import deepcopy
from models.categorydb import editdb

def call(id):
    kdict = deepcopy(config.kdict)
    kdict['pageTitle'] = 'ទំព័រ​កែប្រែ'
    kdict['route'] = 'category'
    kdict['edit'] = True

    categories, count, category = editdb.call(id, kdict['maxItemList'])

    kdict['items'] = categories
    kdict['count'] = count
    kdict['item'] = category
    
    return template('backend/admin.tpl', data=kdict)