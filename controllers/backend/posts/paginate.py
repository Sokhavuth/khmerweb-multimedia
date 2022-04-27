#controllers/backend/posts/paginate.py
import config
from bottle import request
from copy import deepcopy
from models.postdb import paginatedb

def call(page):
    kdict = deepcopy(config.kdict)
    posts = paginatedb.call(page, kdict['maxItemList'])
    items = [post for post in posts]
    
    return {'items':items}