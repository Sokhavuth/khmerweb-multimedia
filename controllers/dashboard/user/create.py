#controllers/dashboard/user/create.py
import uuid, base64
from bottle import request, redirect
from models.userdb import createdb

def call():
    name = request.forms.getunicode('name')
    thumb = request.forms.getunicode('thumb')
    datetime = request.forms.getunicode('datetime')
    email = request.forms.getunicode('email')
    password = request.forms.getunicode('password')
    password = password.encode("utf-8")
    password = base64.b64encode(password)
    edit = request.forms.getunicode('editid')
    content = request.forms.getunicode('content')
    role = request.forms.getunicode('role')
    entries = request.forms.getunicode('entries')

    if not edit:
        id = uuid.uuid4().hex
    else:
        id = edit

    createdb.call(name, thumb, datetime, id, email, password, content, role, entries, edit)

    return redirect('/dashboard/user')