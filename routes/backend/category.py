#routes/backend/category.py
from bottle import Bottle, redirect
from controllers.frontend.login import checkLogged

app = Bottle()

@app.route('/')
def get():
    if checkLogged.call():
        from controllers.backend.categories import get
        return get.call()
    else:
        redirect('/login')

@app.route('/', method="post")
def create():
    if checkLogged.call():
        from controllers.backend.categories import create
        return create.call()
    else:
        redirect('/login')

@app.route('/edit/<id>')
def create(id):
    if checkLogged.call():
        from controllers.backend.categories import edit
        return edit.call(id)
    else:
        redirect('/login')

@app.route('/delete/<id>')
def create(id):
    if checkLogged.call():
        from controllers.backend.categories import delete
        return delete.call(id)
    else:
        redirect('/login')

@app.route('/paginate/<page>')
def create(page):
    if checkLogged.call():
        from controllers.backend.categories import paginate
        return paginate.call(int(page))
    else:
        redirect('/login')