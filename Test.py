import pymongo


client = pymongo.MongoClient("mongodb+srv://tushar_v04:3d0fMui38rF3XHLD@cashflowmanagement.hwbys.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db=client["CashFlowManager"]
userData=db["UserData"]

def signup(user):
    userData.insert_one(user)
    userinfo=userData.find_one(user)
    userid=str(userinfo["_id"])
    print(userid)
    return userid
