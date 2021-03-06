#config.py
import os
#pip install python-dotenv
from dotenv import load_dotenv

load_dotenv()
kdict = {}

kdict['SECRET_KEY'] = os.environ.get('SECRET_KEY')
kdict['MONGODB_URI'] = os.environ.get('MONGODB_URI')

kdict['siteTitle'] = 'ពហុព័ត៌មាន'
kdict['pageTitle'] = 'ទំព័រ​ដ់ើម'
kdict['message'] = ''
kdict['maxItemList'] = 10
kdict['maxRandom'] = 125