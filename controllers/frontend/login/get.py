#controllers/frontend/login/get.py
import config
from copy import deepcopy

def call():
    kdict = deepcopy(config.kdict)
