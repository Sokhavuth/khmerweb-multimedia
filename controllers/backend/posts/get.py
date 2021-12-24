#controllers/frontend/login/get.py
import config
from copy import deepcopy
from bottle import template

def call():
    kdict = deepcopy(config.kdict)
    kdict['pageTitle'] = 'ទំព័រ​ការផ្សាយ'
    kdict['route'] = 'post'

    return template('backend/admin', data=kdict)