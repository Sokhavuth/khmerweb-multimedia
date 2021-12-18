#config.py
import os
#We need to install python-dotenv
from dotenv import load_dotenv

load_dotenv()
kdict = {}

kdict['SECRET_KEY'] = os.environ.get('SECRET_KEY')
kdict['DATABASE_URI'] = os.environ.get('DATABASE_URI')

kdict['siteTitle'] = 'Khmer Web REST API'
kdict['siteLogo'] = 'ទំព័រ​គ្រប់គ្រង'
kdict['message'] = ''
kdict['maxItemList'] = 10