#routes/backend/post.py
from bottle import Bottle, redirect
from controllers.frontend.login import checkLogged

app = Bottle()

@app.route('/')
def get():
    if checkLogged.call():
        from controllers.backend.posts import get
        return get.call()
    else:
        redirect('/login')

@app.route('/', method="post")
def create():
    if checkLogged.call():
        from controllers.backend.posts import create
        return create.call()
    else:
        redirect('/login')

@app.route('/edit/<id>')
def edit(id):
    if checkLogged.call():
        from controllers.backend.posts import edit
        return edit.call(id)
    else:
        redirect('/login')

@app.route('/delete/<id>')
def delete(id):
    if checkLogged.call():
        from controllers.backend.posts import delete
        return delete.call(id)
    else:
        redirect('/login')

@app.route('/paginate/<page>')
def paginate(page):
    if checkLogged.call():
        from controllers.backend.posts import paginate
        return paginate.call(int(page))
    else:
        redirect('/login')