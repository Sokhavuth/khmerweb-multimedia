#routes/frontend/index.py
import config
from bottle import Bottle

app = Bottle()

@app.route('/')
def index():
    return config.kdict['siteTitle']