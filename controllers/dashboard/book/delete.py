#controllers/dashboard/book/delete.py
from bottle import template, redirect
from models.bookdb import deletedb

def call(id):
    deletedb.call(id)
    
    redirect('/dashboard/book')