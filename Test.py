from http import client
import pymongo


client=pymongo.MongoClient("mongodb://localhost:27017/")
print(client)
db=client["CashFlowManager"]
userData=db["UserData"]
def signup(user):
    userData.insert_one(user)
