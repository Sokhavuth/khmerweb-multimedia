#routes/login.py
from bottle import Bottle

app = Bottle()

@app.route('/', method="post")
def checkUser():
    from controllers.login import checkUser
    return checkUser.call()