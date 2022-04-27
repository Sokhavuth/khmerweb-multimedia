#index.py
import sys
from routes.frontend import index
from routes.frontend import login
from routes.backend import admin

app = index.app
app.mount('/login', login.app)
app.mount('/admin', admin.app)

if sys.platform == 'win32':
    app.run(host='localhost', port=7000, debug=True, reloader=True)