from re import sub
import pymongo
from bson import ObjectId

client = pymongo.MongoClient("mongodb+srv://@cashflowmanagement.hwbys.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db=client["CashFlowManager"]
userData=db["UserData"]
billData=db["billData"]
subscriptionData=db["subscriptionData"]


def signup(user):
    userinfo=userData.find_one({"email":user["email"]})
    if(userinfo !=None):
        res={"message":"Email already exists","id":None}
        return res
    else:
        userData.insert_one(user)
        userinfo=userData.find_one(user)
        userid=str(userinfo["_id"])
        res={"message":"Sign up successful","id":userid}
        return res


def login(user):
    userinfo=userData.find_one({"email":user["email"]})
    if(userinfo==None):
        res={"message":"User does'exists","id":None}
    elif(user["password"]!=userinfo["password"]):
        res={"message":"Wrong password","id":None}
    elif(user["password"]==userinfo["password"]):
        res={"message":"Login successful","id":str(userinfo["_id"])}
    else:
        res={"message":"somthing went wrong plz try again","id":None}
    
    return res

def bill(billinfo):
    billData.insert_one(billinfo)
    info=billData.find_one(billinfo)
    billid=str(info["_id"])
    return ({"message":"Bill entered","id":billid})

def subscription(info):
    subscriptionData.insert_one(info)
    subs=subscriptionData.find_one(info)
    subsid=str(subs["_id"])
    return ({"message":"Subscription added","id":subsid})

def getuser(uid):
    if(len(uid)!=24):
        return {"id":None}
    user=userData.find_one({"_id":ObjectId(uid)},{"_id":0})
    if(user==None):
        return {"id":None}
    user["id"]=uid
    return (user)

def getbills(uid):
    bill=billData.find({"uid":uid})
    data={"data":[]}
    for item in bill:
        item["id"]=str(item.pop("_id"))
        data["data"].append(item)
    if(len(data["data"])==0):
        return {"data":None}
    return (data)

def getsubscriptions(uid):
    subs=subscriptionData.find({"uid":uid})
    if(subs==None):
        return {"data":None}
    data={"data":[]}
    for item in subs:
        item["id"]=str(item.pop("_id"))
        data["data"].append(item)
    if(len(data["data"])==0):
        return {"data":None}
    return (data)

def getbill(uid,id):
    bill=billData.find_one({"_id":int(id),"uid":uid},{"_id":0})
    if(bill==None):
        return {"id":None}
    bill["id"]=int(id)
    return (bill)

def getsubscription(uid,id):
    subs=subscriptionData.find_one({"_id":int(id),"uid":uid},{"_id":0})
    if(subs==None):
        return {"id":None}
    subs["id"]=int(id)
    return (subs)