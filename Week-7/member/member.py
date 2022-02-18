from flask import request
from flask import render_template
from flask import redirect
from flask import session
from flask import url_for
from flask import Blueprint
import db

app2=Blueprint("member", __name__, static_folder="static", static_url_path="/member/static", template_folder="templates")

app2.secret_key="ImportantKey"#設定session的密鑰

@app2.route("/member/", methods=["GET", "POST"])
def success():
    if(session["status"]=="已登入"):
        uname=session["name"]
        return render_template("SuccessPage.html", name=uname)
    else:
        return redirect(url_for("HomePage"))

@app2.route("/signin", methods=["GET", "POST"])
def signin():
    conn=db.con_pool.get_connection()
    mycursor=conn.cursor()
    session["status"]="未登入"
    account=request.form["account"]
    password=request.form["password"]
    session["account"]=account
    session["password"]=password
    check_account="SELECT*FROM member WHERE username=%s"
    ca=[account]
    mycursor.execute(check_account, ca)
    result=mycursor.fetchone()
    conn.close()
    if(result==None):
        if session["account"]=="" and session["password"]=="":
            Fmessage="請輸入帳號密碼"
        else:
            Fmessage="帳號密碼輸入錯誤"
        return redirect(url_for("fail.fail", message=Fmessage))
        #("fail",message=Fmessage)附帶query string至error/
    elif(account==result[2] and password==result[3] and request.method=="POST"):
        session["name"]=result[1]
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