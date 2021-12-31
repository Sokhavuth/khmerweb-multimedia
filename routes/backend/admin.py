#routes/backend/admin.py
from bottle import Bottle

import bottle
bottle.BaseRequest.MEMFILE_MAX = 1024 * 1024

app = Bottle()

from routes.backend import post
app.mount('/post', post.app)

from routes.backend import category
app.mount('/category', category.app)