#routes/dashboard.py
import config
from bottle import Bottle, redirect
from controllers.login import checkLogged

import bottle
bottle.BaseRequest.MEMFILE_MAX = 1024 * 1024

app = Bottle()

@app.route('/')
def index():
    if checkLogged.call():
        from controllers.dashboard import index
        return index.call()
    else:
        redirect('/')

@app.route('/logout')
def logout():
    from controllers.dashboard import logout
    logout.call()

from routes import category
app.mount('/category', category.app)

from routes import post
app.mount('/post', post.app)

from routes import book
app.mount('/book', book.app)

from routes import upload
app.mount('/upload', upload.app)

from routes import user
app.mount('/user', user.app)