import pymongo

client = pymongo.MongoClient("mongodb+srv://tushar_v04:3d0fMui38rF3XHLD@cashflowmanagement.hwbys.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db=client["CashFlowManager"]
userData=db["UserData"]
billData=db["billData"]


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