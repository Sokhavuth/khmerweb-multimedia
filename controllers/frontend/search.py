#controllers/frontend/post.py
import config
from copy import deepcopy
from bottle import template, request
from models.postdb import searchdb

def call():
    kdict = deepcopy(config.kdict)
    kdict['pageTitle'] = 'ទំព័រ​ស្វែង​រក'
    kdict['route'] = 'search'
    q = request.forms.getunicode('q')
    kdict['posts'] = searchdb.call(40,q)

    return template('frontend/index', data=kdict)