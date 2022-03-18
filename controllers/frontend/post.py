#controllers/frontend/post.py
import config
from copy import deepcopy
from bottle import template
from models.postdb import getPostdb, random
from controllers.frontend.login import checkLogged

def call(id):
    kdict = deepcopy(config.kdict)
    kdict['pageTitle'] = 'ទំព័រ​ការផ្សាយ'
    kdict['route'] = 'post'
    kdict['post'] = getPostdb.call(id)
    kdict['posts'] = random.call(5,id)
    kdict['user'] = checkLogged.call()

    return template('frontend/index', data=kdict)