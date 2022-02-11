from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from flask import session
from flask import url_for
from flask import Blueprint
import mysql.connector

app4=Blueprint("signup", __name__, static_folder="static", static_url_path="/signup/static", template_folder="templates")

app4.secret_key="ImportantKey"#設定session的密鑰

mydb=mysql.connector.connect(
    host="localhost",
    port="3400",
    user="root",
    password="abc123456",
    database="W6"    
)
mycursor=mydb.cursor();

@app4.route("/signup", methods=["POST", "GET"])
def signup():
    name=request.form["name"]
    account=request.form["account"]
    password=request.form["password"]
    check_account="SELECT*FROM member WHERE username=%s"
    ca=[account]
    mycursor.execute(check_account, ca)
    result=mycursor.fetchone()
    if(name!="" or account!="" or password!=""):
        if(result==None):
            insert_sql="INSERT INTO member (name, username, password) VALUES(%s, %s, %s)"
            value=(name, account, password)
            mycursor.execute(insert_sql, value)
            mydb.commit()
            return redirect(url_for("signup.signupSucess"))
            #Blueprint
        else:
            Fmessage="帳號已被註冊"
            return redirect(url_for("fail.fail", message=Fmessage))
    else:
        Fmessage="請填寫所有欄位"
        return redirect(url_for("fail.fail", message=Fmessage))
 
@app4.route("/signupSuccess", methods=["GET"])
def signupSucess():
    return render_template("SignUpSuccess.html")