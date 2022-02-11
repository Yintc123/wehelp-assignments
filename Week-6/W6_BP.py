from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from flask import session
from flask import url_for
import mysql.connector
from member.member import app2
from fail.fail import app3
from signup.signup import app4
#主要執行檔不用importBlueprint

app=Flask(__name__, static_folder="static", static_url_path="/static")

app.secret_key="ImportantKey"#設定session的密鑰

mydb=mysql.connector.connect(
    host="localhost",
    port="3400",
    user="root",
    password="abc123456",
    database="W6"    
)
mycursor=mydb.cursor();

@app.route("/")
def HomePage():
    if session.get("status") == None:
        session["status"]="未登入"
    return render_template("HomePage.html", Status=session.get("status"))

app.register_blueprint(app2)
app.register_blueprint(app3)
app.register_blueprint(app4)

if __name__ == "__main__":
    app.debug=True
    app.run(port=3000)