#controllers/backend/posts/create.py
import uuid, config
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
    authorID = request.get_cookie('userID', secret=config.kdict['SECRET_KEY'])

    if not edit:
        id = uuid.uuid4().hex
    else:
        id = edit
    
    userRole = request.get_cookie('userRole', secret=config.kdict['SECRET_KEY'])
    if userRole != 'visitor':
        createdb.call(title, thumb, datetime, id, edit, content, category, entries, authorID)

    return redirect('/admin/post')