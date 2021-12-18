#controllers/dashboard/index.py
import config
from bottle import template
from copy import deepcopy
from models.categorydb import getdb
from controllers.dashboard.post import get

def call():
    kdict = deepcopy(config.kdict)
    kdict['siteLogo'] = 'ទំព័រ​ការផ្សាយ'
    kdict['route'] = 'post'

    kdict['categories'] = getdb.call('all')
    posts, count = get.call()
    kdict['items'] = posts
    kdict['count'] = count

    return template('dashboard/index.tpl', data=kdict)
