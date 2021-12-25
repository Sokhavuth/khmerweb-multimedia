#routes/frontend/index.py
import config
from bottle import Bottle, static_file

app = Bottle()

@app.route('/static/images/<filename>')
def loadImage(filename):
    return static_file(filename, root='./asset/img')

@app.route('/static/styles/<filename>')
def loadStyle(filename):
    return static_file(filename, root='./asset/css')

@app.route('/static/styles/partials/<filename>')
def loadStylePartial(filename):
    return static_file(filename, root='./asset/css/partials')

@app.route('/static/styles/highlight/styles/<filename>')
def loadHighLightStylesScript(filename):
    return static_file(filename, root='./asset/js/highlight/styles')

@app.route('/static/scripts/<filename>')
def loadScript(filename):
    return static_file(filename, root='./asset/js')

@app.route('/static/scripts/ckeditor/<filename>')
def loadCKEditorScript(filename):
    return static_file(filename, root='./asset/js/ckeditor')

@app.route('/static/fonts/<filename>')
def loadFont(filename):
    return static_file(filename, root='./asset/font')

@app.route('/static/uploads/<filename>')
def loadFont(filename):
    return static_file(filename, root='./asset/uploads')

@app.route('/')
def index():
    return config.kdict['pageTitle']