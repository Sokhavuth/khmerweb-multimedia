#controllers/dashboard/post/get.py
import config
from bottle import template
from copy import deepcopy
from models.postdb import getdb

def call():
    kdict = deepcopy(config.kdict)
    kdict['siteLogo'] = 'ទំព័រ​ការផ្សាយ'
    kdict['route'] = 'index'

    posts, count = getdb.call(kdict['maxItemList'])

    return posts, count