#controllers/backend/categories/create.py
import uuid, config
from bottle import request, redirect
from models.categorydb import createdb

def call():
    name = request.forms.getunicode('name')
    link = request.forms.getunicode('link')
    datetime = request.forms.getunicode('datetime')
    edit = request.forms.getunicode('editid')

    if not edit:
        id = uuid.uuid4().hex
    else:
        id = edit

    userRole = request.get_cookie('userRole', secret=config.kdict['SECRET_KEY'])
    if userRole != 'visitor':
        createdb.call(name, link, datetime, id, edit)

    return redirect('/admin/category')