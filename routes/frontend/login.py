#routes/frontend/login.py
from bottle import Bottle, redirect
from controllers.frontend.login import checkLogged

app = Bottle()

@app.route('/')
def index():
    if checkLogged.call():
        redirect('/admin/post')
    else:
        from controllers.frontend.login import get
        return get.call()

@app.route('/', method="post")
def checkUser():
    from controllers.frontend.login import checkUser
    return checkUser.call()

@app.route('/logout')
def logout():
    from controllers.frontend.login import logout
    return logout.call()