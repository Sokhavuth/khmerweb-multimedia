#controllers/dashboard/category/get.py
import config
from bottle import template
from copy import deepcopy
from models.categorydb import getdb

def call():
    kdict = deepcopy(config.kdict)
    kdict['siteLogo'] = 'ទំព័រ​ជំពូក'
    kdict['route'] = 'category'

    categories, count = getdb.call(kdict['maxItemList'])

    kdict['items'] = categories
    kdict['count'] = count
    
    return template('dashboard/index.tpl', data=kdict)
