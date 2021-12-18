#controllers/dashboard/post/create.py
import uuid
from bottle import request, redirect
from models.postdb import createdb

def call():
    title = request.forms.getunicode('title')
    thumb = request.forms.getunicode('thumb')
    datetime = request.forms.getunicode('datetime')
    edit = request.forms.getunicode('editid')
    content = request.forms.getunicode('content')
    category = request.forms.getunicode('category')
    entries = request.forms.getunicode('entries')

    if not edit:
        id = uuid.uuid4().hex
    else:
        id = edit

    createdb.call(title, thumb, datetime, id, edit, content, category, entries)

    return redirect('/dashboard')