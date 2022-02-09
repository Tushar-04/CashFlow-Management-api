from cmath import isnan
from pickle import NONE
from flask import Flask, request,jsonify
import Test
from flask_httpauth import HTTPBasicAuth

app=Flask(__name__)
auth=HTTPBasicAuth()
USER_DATA={
    "admin":"WrongPassword"
}
@auth.verify_password
def verify(username,password):
    if(USER_DATA.get(username)==password):
        return True
    else:
        return False

@app.route("/",methods = ['GET'])
@auth.login_required
def default():
    return jsonify({"message":"Welcome to Cash flow manager api"})
    
@app.route("/signup" ,methods = ['POST'])
@auth.login_required
def signup():
    user=dict(request.json)
    res=Test.signup(user)
    return jsonify(res)

@app.route("/login" ,methods = ['POST'])
@auth.login_required
def login():
    res=Test.login(request.json)
    return jsonify(res)

@app.route("/bill" ,methods = ['POST'])
@auth.login_required
def bill():
    res=Test.bill(request.json)
    return jsonify(res)

@app.route("/subscription" ,methods = ['POST'])
@auth.login_required
def subscription():
    res=Test.subscription(request.json)
    return jsonify(res)

@app.route("/getuser" ,methods = ['GET'])
@auth.login_required
def getuser():
    uid=request.args.get("id")
    res=Test.getuser(uid)
    return jsonify(res)

@app.route("/getbills" ,methods = ['GET'])
@auth.login_required
def getbills():
    uid=request.args.get("uid")
    id=request.args.get("bid")
    if(not id):
        res=Test.getbills(uid)
    else:
        res=Test.getbill(uid,id)
    return jsonify(res)


@app.route("/getsubscriptions" ,methods = ['GET'])
@auth.login_required
def getsubscriptions():
    uid=request.args.get("uid")
    id=request.args.get("sid")
    if(not id):
        res=Test.getsubscriptions(uid)
    else:
        res=Test.getsubscription(uid,id)
    return jsonify(res)


if __name__ == '__main__':
    app.run(debug=True)