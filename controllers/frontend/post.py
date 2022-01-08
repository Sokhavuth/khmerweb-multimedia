#controllers/frontend/post.py
import config, json
from copy import deepcopy
from bottle import template
from models.postdb import getPostdb, random

def call(id):
    kdict = deepcopy(config.kdict)
    kdict['pageTitle'] = 'ទំព័រ​ការផ្សាយ'
    kdict['route'] = 'post'
    kdict['post'] = getPostdb.call(id)
    kdict['posts'] = random.call(5)

    return template('frontend/index', data=kdict)