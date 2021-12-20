#index.py
import sys
from routes.frontend import index
from routes.frontend import login

app = index.app
app.mount('/login', login.app)

if sys.platform == 'win32':
    app.run(host='localhost', port=7000, debug=True, reloader=True)
