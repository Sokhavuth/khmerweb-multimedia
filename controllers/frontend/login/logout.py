#controllers/frontend/login/logout.py
import config
from bottle import response, redirect

def call():
    response.delete_cookie('userID', path='/', secret=config.kdict['SECRET_KEY'])
    redirect('/')