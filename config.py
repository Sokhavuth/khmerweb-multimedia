#config.py
import os
#pip install python-dotenv
from dotenv import load_dotenv

load_dotenv()
kdict = {}

kdict['SECRET_KEY'] = os.environ.get('SECRET_KEY')
kdict['MONGODB_URI'] = os.environ.get('MONGODB_URI')

kdict['siteTitle'] = 'Khmer Web Multimedia'
kdict['siteLogo'] = 'ទំព័រ​ដ់ើម'
kdict['message'] = ''
kdict['maxItemList'] = 10