from http import client
import ssl
import pymongo


client = pymongo.MongoClient("mongodb+srv://tushar_v04:3d0fMui38rF3XHLD@cashflowmanagement.hwbys.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
print(client)
db=client["CashFlowManager"]
userData=db["UserData"]

def signup(user):
    userData.insert_one(user)
    userinfo=userData.find(user)
    userid=userinfo["_id"]
    return userid
