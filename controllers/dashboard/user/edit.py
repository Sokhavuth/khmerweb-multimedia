#controllers/dashboard/user/edit.py
import config
from bottle import template
from copy import deepcopy
from models.userdb import getdb, editdb

def call(id):
    kdict = deepcopy(config.kdict)
    kdict['siteLogo'] = 'ទំព័រ​អ្នក​ប្រើប្រាស់'
    kdict['route'] = 'user'
    kdict['edit'] = 'edit'

    users, count = getdb.call(kdict['maxItemList'])
    item, userid = editdb.call(id)

    kdict['items'] = users
    kdict['count'] = count
    kdict['userid'] = userid
    kdict['item'] = item
    
    return template('dashboard/index.tpl', data=kdict)