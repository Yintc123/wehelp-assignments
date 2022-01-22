from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from flask import session
from flask import url_for

app=Flask(__name__, static_folder="static", static_url_path="/static")

app.secret_key="ImportantKey"#設定session的密鑰

@app.route("/")
def HomePage():
    if session.get("status") == None:
        session["status"]="未登入"
    return render_template("HomePage.html", Status=session.get("status"))

@app.route("/member/", methods=["GET", "POST"])
def success():
    if(session["status"]=="已登入"):
        return render_template("SuccessPage.html", name=session["account"])
    else:
        return redirect(url_for("HomePage"))

@app.route("/error/", methods=["GET"])
def fail():
    Fmessage=request.args.get("message")#將query stirng的訊息存至Fmessage
    return render_template("FailPage.html", FailMessage=Fmessage)

@app.route("/signin", methods=["GET", "POST"])
def signin():
    session["status"]="未登入"
    account=request.form["account"]
    password=request.form["password"]
    session["account"]=account
    session["password"]=password
    if(account=="test" and password=="test" and request.method=="POST"):
        session["status"]="已登入"
        return redirect(url_for("success"))
    else:
        if session["account"]=="" and session["password"]=="":
            Fmessage="請輸入帳號密碼"
        else:
            Fmessage="帳號密碼輸入錯誤"
        return redirect(url_for("fail", message=Fmessage))
        #("fail",message=Fmessage)附帶query string至error/ 

@app.route("/signout", methods=["GET"])
def signout():
    session["status"]="未登入"
    session.pop("account", None)
    session.pop("password", None)
    return redirect(url_for("HomePage"))  

if __name__ == "__main__":
    app.debug=True
    app.run(port=3000)