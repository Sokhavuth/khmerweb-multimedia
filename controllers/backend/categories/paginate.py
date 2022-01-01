#controllers/backend/categories/paginate.py
import config
from bottle import request
from copy import deepcopy
from models.categorydb import paginatedb

def call(page):
    kdict = deepcopy(config.kdict)
    categories = paginatedb.call(page, kdict['maxItemList'])
    items = [category for category in categories]
    
    return {'items':items}