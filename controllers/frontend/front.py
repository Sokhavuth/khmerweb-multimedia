#controllers/frontend/front.py
import config
from copy import deepcopy
from bottle import template

def call():
    kdict = deepcopy(config.kdict)
    kdict['pageTitle'] = 'ទំព័រ​ដើម'
    kdict['route'] = 'front'

    return template('frontend/index', data=kdict)