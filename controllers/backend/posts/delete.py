#controllers/backend/posts/delete.py
from bottle import redirect
from models.postdb import deletedb

def call(id):
    deletedb.call(id)

    redirect('/admin/post')