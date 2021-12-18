#index.py
import sys
from routes import index

app = index.app

if sys.platform == 'win32':
    app.run(host='localhost', port=7000, debug=True, reloader=True)
    