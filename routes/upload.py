#routes/upload.py
from bottle import Bottle, redirect
from controllers.login import checkLogged

import bottle
bottle.BaseRequest.MEMFILE_MAX = 1024 * 1024

app = Bottle()

@app.route('/')
def index():
    if checkLogged.call():
        from controllers.dashboard.upload import get
        return get.call()
    else:
        redirect('/')

@app.route('/', method='post')
def index():
    if checkLogged.call():
        from controllers.dashboard.upload import create
        return create.call()
    else:
        redirect('/')