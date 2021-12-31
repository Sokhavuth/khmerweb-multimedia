#controllers/backend/posts/edit.py
import config
from bottle import template
from copy import deepcopy
from models.postdb import editdb

def call(id):
    kdict = deepcopy(config.kdict)
    kdict['pageTitle'] = 'ទំព័រ​កែប្រែ'
    kdict['route'] = 'post'
    kdict['edit'] = True

    posts, count, post = editdb.call(id, kdict['maxItemList'])

    kdict['items'] = posts
    kdict['count'] = count
    kdict['item'] = post
    
    return template('backend/admin.tpl', data=kdict)