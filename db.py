from bson import ObjectId # For ObjectId to work
from pymongo import MongoClient
import os

class DB():
    mongoUrl=""
    name=""
    password=""
    dbName=""
    client=""
    db=""
    coll=""

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

    def add(self, member):
        self.coll.insert(member.__dict__)

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