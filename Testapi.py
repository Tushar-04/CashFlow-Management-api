from flask import Flask, request
import Test

app=Flask(__name__)

@app.route("/",methods = ['GET'])
def default():
    return ({"message":"Welcome to Cash flow manager api"})
    
@app.route("/signup" ,methods = ['POST'])
def signup():
    user=dict(request.json)
    res=Test.signup(user)
    return res

@app.route("/login" ,methods = ['POST'])
def login():
    res=Test.login(request.json)
    return res

@app.route("/bill" ,methods = ['POST'])
def bill():
    res=Test.bill(request.json)
    return res

if __name__ == '__main__':
    app.run(debug=True)