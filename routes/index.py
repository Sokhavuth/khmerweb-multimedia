#routes/index.py
import config
from copy import deepcopy
from bottle import Bottle

app = Bottle()

@app.route('/')
def index():
    return 'ទំព័រ​ដើម'