#controllers/dashboard/category/create.py
import uuid
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

    createdb.call(name, link, datetime, id, edit)

    return redirect('/dashboard/category')
