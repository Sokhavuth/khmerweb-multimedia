#controllers/frontend/login/get.py
import config
from copy import deepcopy
from bottle import template
from models.postdb import getdb

def call():
    kdict = deepcopy(config.kdict)
    kdict['pageTitle'] = 'ទំព័រ​ការផ្សាយ'
    kdict['route'] = 'post'
    posts, count = getdb.call(kdict['maxItemList'])
    kdict['items'] = posts
    kdict['count'] = count

    return template('backend/admin', data=kdict)