from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from flask import session
from flask import url_for
from flask import Blueprint
import mysql.connector

app2=Blueprint("member", __name__, static_folder="static", static_url_path="/member/static", template_folder="templates")

app2.secret_key="ImportantKey"#設定session的密鑰

mydb=mysql.connector.connect(
    host="localhost",
    port="3400",
    user="root",
    password="abc123456",
    database="W6"    
)
mycursor=mydb.cursor();

@app2.route("/member/", methods=["GET", "POST"])
def success():
    if(session["status"]=="已登入"):
        account=session["account"]
        check_account="SELECT*FROM member WHERE username=%s"
        ca=[account]
        mycursor.execute(check_account, ca)
        result=mycursor.fetchone()
        return render_template("SuccessPage.html", name=result[1])
    else:
        return redirect(url_for("HomePage"))

@app2.route("/signin", methods=["GET", "POST"])
def signin():
    session["status"]="未登入"
    account=request.form["account"]
    password=request.form["password"]
    session["account"]=account
    session["password"]=password
    check_account="SELECT*FROM member WHERE username=%s"
    ca=[account]
    mycursor.execute(check_account, ca)
    result=mycursor.fetchone()
    if(result==None):
        if session["account"]=="" and session["password"]=="":
            Fmessage="請輸入帳號密碼"
        else:
            Fmessage="帳號密碼輸入錯誤"
        return redirect(url_for("fail.fail", message=Fmessage))
        #("fail",message=Fmessage)附帶query string至error/
    elif(account==result[2] and password==result[3] and request.method=="POST"):
        session["status"]="已登入"
        return redirect(url_for("member.success"))
    else:
        Fmessage="帳號密碼輸入錯誤"
        return redirect(url_for("fail.fail", message=Fmessage))

@app2.route("/signout", methods=["GET"])
def signout():
    session["status"]="未登入"
    session.pop("account", None)
    session.pop("password", None)
    return redirect(url_for("HomePage"))