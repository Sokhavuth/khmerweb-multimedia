#controllers/dashboard/post/delete.py
from bottle import template, redirect
from models.postdb import deletedb

def call(id):
    deletedb.call(id)
    
    redirect('/dashboard')