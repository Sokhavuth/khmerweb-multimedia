#controllers/dashboard/user/delete.py
from bottle import redirect
from models.userdb import deletedb

def call(id):
    deletedb.call(id)
    
    redirect('/dashboard/user')