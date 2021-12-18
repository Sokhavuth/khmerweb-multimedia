#controllers/dashboard/logout.py
import config
from bottle import request, response, redirect

def call():
    response.delete_cookie('logged-in', path='/', secret=config.kdict['SECRET_KEY'])
    redirect('/')