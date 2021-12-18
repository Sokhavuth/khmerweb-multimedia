#controllers/dashboard/post/create.py
import uuid
from bottle import request, redirect
from models.bookdb import createdb

def call():
    title = request.forms.getunicode('title')
    thumb = request.forms.getunicode('thumb')
    datetime = request.forms.getunicode('datetime')
    edit = request.forms.getunicode('editid')
    content = request.forms.getunicode('content')
    chapter = request.forms.getunicode('chapter')
    entries = request.forms.getunicode('entries')
    bookTitle = request.forms.getunicode('book_title')

    if not edit:
        id = uuid.uuid4().hex
    else:
        id = edit

    createdb.call(title, thumb, datetime, id, edit, content, chapter, entries, bookTitle)

    return redirect('/dashboard/book')