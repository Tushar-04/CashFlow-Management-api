from flask import Flask, request
import Test
app=Flask(__name__)
@app.route("/",methods = ['GET'])
def default():
    return ({"Message":"Welcome to Cash flow manager api"})
    
@app.route("/signup" ,methods = ['POST'])
def signup():
    user=dict(request.json)
    userid=Test.signup(user)
    res={"message":"Sign up successful","id":userid}
    return res
@app.route("/login" ,methods = ['POST'])
def login():
    res=Test.login(request.json)
    return res
if __name__ == '__main__':
    app.run(debug=True)