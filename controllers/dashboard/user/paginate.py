#controllers/dashboard/user/paginate.py
import config
from bottle import request
from copy import deepcopy
from models.userdb import paginatedb

def call(page):
    kdict = deepcopy(config.kdict)
    users = paginatedb.call(page, kdict['maxItemList'])
    
    return {'items':users}