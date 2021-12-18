#controllers/dashboard/upload/get.py
import config
from bottle import template
from copy import deepcopy

def call():
    kdict = deepcopy(config.kdict)
    kdict['siteLogo'] = 'ទំព័រ​ Upload'
    kdict['route'] = 'upload'

    return template('dashboard/index.tpl', data=kdict)