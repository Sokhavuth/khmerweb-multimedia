#controllers/login/checkUser.py
import config, base64
from copy import deepcopy
from bottle import template, request, response, redirect
from models.userdb import checkUserDB

def call():
    kdict = deepcopy(config.kdict)
    password = request.forms.getunicode('password')
    password = password.encode("utf-8")
    password = base64.b64encode(password)
    email = request.forms.getunicode('email')
    
    user = checkUserDB.call(email, password)
    
    if user:
        kdict["siteLogo"] = 'ទំព័រ​គ្រប់គ្រង'
        response.set_cookie('logged-in', user[3], path='/', secret=kdict['SECRET_KEY'])
        return redirect('/dashboard')
    else:
        kdict['message'] = 'អ្នក​គ្មាន​ឈ្មោះ​ក្នុង​បញ្ជី​ទេ'
        return template('index', data=kdict)
