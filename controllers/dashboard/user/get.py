#controllers/dashboard/user/get.py
import config
from bottle import template
from copy import deepcopy
from models.userdb import getdb

def call():
    kdict = deepcopy(config.kdict)
    kdict['siteLogo'] = 'ទំព័រ​អ្នក​ប្រើប្រាស់'
    kdict['route'] = 'user'

    users, count = getdb.call(kdict['maxItemList'])
    kdict['items'] = users
    kdict['count'] = count

    return template('dashboard/index.tpl', data=kdict)