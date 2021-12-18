#controllers/dashboard/upload/create.py
import uuid, os, config
from bottle import request, template
from copy import deepcopy

def call():
    kdict = deepcopy(config.kdict)
    kdict['siteLogo'] = 'ទំព័រ​ Upload'
    kdict['route'] = 'upload'
    kdict['uploaded'] = 'uploaded'

    upload = request.files.get('upload')
    name, ext = os.path.splitext(upload.filename)
    if ext not in ('.png','.jpg','.jpeg'):
        return 'File extension not allowed.'

    id = uuid.uuid4().hex
    upload.filename = id + '_' + name + ext
    kdict['url'] = '/static/uploads/' + upload.filename

    save_path = 'asset/uploads'
    upload.save(save_path)

    return template('dashboard/index.tpl', data=kdict)