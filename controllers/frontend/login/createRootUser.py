#controllers/frontend/login/createRootUser.py
#pip install pymongo
#pip install bcrypt
import uuid, config, pymongo, bcrypt

def call():
    myclient = pymongo.MongoClient(config.kdict['MONGODB_URI'])
    mydb = myclient["multimedia"]
    mycol = mydb["users"]

    password = b"Guest2021"
    hashedPassword = bcrypt.hashpw(password, bcrypt.gensalt())

    user = { 
        "userID": uuid.uuid4().hex, 
        "email": "guest@khmerweb.app",
        "username": "guest",
        "password": hashedPassword,
        "role":"visitor",
        "thumb":"",
        "info":"",
        "video":"",
        "date":""
     }

    mycol.insert_one(user)
