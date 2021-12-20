#routes/frontend/login.py
from bottle import Bottle

app = Bottle()

@app.route('/')
def index():
    from controllers.frontend.login import get
    return get.call()

@app.route('/', method="post")
def checkUser():
    from controllers.frontend.login import checkUser
    return checkUser.call()