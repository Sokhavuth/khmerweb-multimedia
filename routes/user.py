#routes/user.py
from bottle import Bottle, redirect
from controllers.login import checkLogged

import bottle
bottle.BaseRequest.MEMFILE_MAX = 1024 * 1024

app = Bottle()

@app.route('/')
def index():
    if checkLogged.call():
        from controllers.dashboard.user import get
        return get.call()
    else:
        redirect('/')

@app.route('/', method='post')
def index():
    if checkLogged.call():
        from controllers.dashboard.user import create
        return create.call()
    else:
        redirect('/')

@app.route('/edit/<id>')
def edit(id):
    if checkLogged.call():
        from controllers.dashboard.user import edit
        return edit.call(id)
    else:
        redirect('/')

@app.route('/delete/<id>')
def delete(id):
    if checkLogged.call():
        from controllers.dashboard.user import delete
        return delete.call(id)
    else:
        redirect('/')

@app.route('/paginate/<page>')
def paginate(page):
    if checkLogged.call():
        from controllers.dashboard.user import paginate
        return paginate.call(int(page))
    else:
        redirect('/')