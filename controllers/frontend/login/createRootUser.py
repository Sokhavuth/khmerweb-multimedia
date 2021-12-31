#controllers/frontend/login/createRootUser.py
#pip install pymongo
#pip install bcrypt
import uuid, config, pymongo, bcrypt

def call():
    myclient = pymongo.MongoClient(config.kdict['MONGODB_URI'])
    mydb = myclient["multimedia"]
    mycol = mydb["users"]

    password = b"Sokhavuth2021"
    hashedPassword = bcrypt.hashpw(password, bcrypt.gensalt())

    user = { 
        "userID": uuid.uuid4().hex, 
        "email": "sokhavuth@khmerweb.app",
        "username": "Sokhavuth",
        "password": hashedPassword,
        "role":"Author",
        "thumb":"",
        "info":"",
        "video":"",
        "date":""
     }

    mycol.insert_one(user)
