#controllers/frontend/front.py
import config
from copy import deepcopy
from bottle import template
from models.postdb import random

def call():
    kdict = deepcopy(config.kdict)
    kdict['pageTitle'] = 'ទំព័រ​ដើម'
    kdict['route'] = 'front'
    kdict['posts'] = random.call(kdict['maxRandom'])

    return template('frontend/index', data=kdict)