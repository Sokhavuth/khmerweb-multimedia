#controllers/backend/categories/delete.py
from bottle import redirect
from models.categorydb import deletedb

def call(id):
    deletedb.call(id)

    redirect('/admin/category')