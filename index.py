#index.py
import sys
from routes import index
from routes import login
from routes import dashboard

app = index.app
app.mount('/login', login.app)
app.mount('/dashboard', dashboard.app)

if sys.platform == 'win32':
    app.run(host='localhost', port=7000, debug=True, reloader=True)