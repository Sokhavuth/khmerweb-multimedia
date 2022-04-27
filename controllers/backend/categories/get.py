#controllers/backend/categories/get.py
import config
from copy import deepcopy
from bottle import template
from models.categorydb import getdb

def call():
    kdict = deepcopy(config.kdict)
    kdict['pageTitle'] = 'ទំព័រ​ជំពូក'
    kdict['route'] = 'category'
    categories, count = getdb.call(kdict['maxItemList'])
    kdict['items'] = categories
    kdict['count'] = count
    
    return template('backend/admin', data=kdict)