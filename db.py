from bson import ObjectId # For ObjectId to work
from pymongo import MongoClient
import os
import genbarcode as QR
try:
    import configparser
except:
    from six.moves import configparser
config = configparser.ConfigParser()
config.read('config.txt')

class DB():
    mongoUrl = config.get('DB','mongoUrl')
    print(mongoUrl)
    name = config.get('DB','name')
    password = config.get('DB','password')
    dbName = config.get('DB','dbName')
    collName = config.get('DB','collName')
    # mongoUrl = "https://yearendl9.documents.azure.com:443/?ssl=true"
    # mongoUrl = "mongodb://yearendl9:DDpFHkFDV1jiUhejE8B22GgwkNjfv5M3PUGSDbJHscbUckJ6PCPrBrYgAckxRJFizgIC1OiEPUeXyFFPxRUmnQ==@yearendl9.documents.azure.com:10255/?ssl=true&replicaSet=globaldb"
    # name = "yearendl9"
    # password = 'DDpFHkFDV1jiUhejE8B22GgwkNjfv5M3PUGSDbJHscbUckJ6PCPrBrYgAckxRJFizgIC1OiEPUeXyFFPxRUmnQ=='
    # dbName = "yvonne"
    # collName= "test"
    client = None
    db = None
    coll = None

    def connect(self):
        self.client = MongoClient(self.mongoUrl) # host uri 
        self.db = self.client[self.dbName] # Select the database
        self.db.authenticate(name=self.name,password=self.password)
        self.coll = self.db[self.collName]

    def close(self):
        self.client.close()

class Member():
    name = None
    alias = None
    department = None
    email = None
    cuisine = None
    accompany = None

    def __init__(self, name, alias, department, email, cuisine, accompany):
        self.name = name
        self.alias = alias
        self.department = department
        self.email = email
        self.cuisine = cuisine
        self.accompany = accompany

class RegisterDB(DB):

    def __init__(self):
        self.connect()

    def register(self, name, alias, department, email, cuisine, accompany):
        new_member = Member(name, alias, department, email, cuisine, accompany)
        self.coll.insert(new_member.__dict__)
        qrcode = QR.gen(new_member)
        print('register done')

    def remove(self, alias):
        self.coll.remove({"alias": alias})

    def list(self):
        memberList = self.coll.find()
        for m in memberList: print(m)

"""
# test case
member = Member('real-aaa', 'aaa', 'bbb@mail.com', 'apple', 'onefriend')
rdb = RegisterDB()
rdb.add(member)
rdb.list()
print('end')
"""