#controllers/dashboard/category/paginate.py
import config
from bottle import request
from copy import deepcopy
from models.categorydb import paginatedb

def call(page):
    kdict = deepcopy(config.kdict)
    categories = paginatedb.call(page, kdict['maxItemList'])
    
    return {'items':categories}
