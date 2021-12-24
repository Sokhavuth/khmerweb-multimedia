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