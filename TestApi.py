from flask import Flask, request
import Test
app=Flask(__name__)
@app.route("/signup" ,methods = ['POST'])
def signup():
    #Test.signup()
    user=dict(request.form)
    Test.signup(user)
    return "Sign up successful"


if __name__ == '__main__':
    app.run(debug=True)