#controllers/dashboard/post/edit.py
import config
from bottle import template
from copy import deepcopy
from models.postdb import getdb, editdb

def call(id):
    kdict = deepcopy(config.kdict)
    kdict['siteLogo'] = 'ទំព័រ​ការផ្សាយ'
    kdict['route'] = 'post'
    kdict['edit'] = 'edit'

    posts, count = getdb.call(kdict['maxItemList'])
    item, categories = editdb.call(id)

    kdict['items'] = posts
    kdict['categories'] = categories
    kdict['count'] = count
    kdict['item'] = item
    
    return template('dashboard/index.tpl', data=kdict)
