#routes/frontend/front.py
from bottle import Bottle

app = Bottle()

@app.route('/')
def index():
    from controllers.frontend import front
    front.call()