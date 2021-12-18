#controllers/dashboard/book/paginate.py
import config
from bottle import request
from copy import deepcopy
from models.bookdb import paginatedb

def call(page):
    kdict = deepcopy(config.kdict)
    books = paginatedb.call(page, kdict['maxItemList'])
    
    return {'items':books}