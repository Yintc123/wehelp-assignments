from flask import Flask
from flask import render_template
from flask import session
from member.member import app2
from fail.fail import app3
from signup.signup import app4
from api.api import app5
#主要執行檔不用importBlueprint

app=Flask(__name__, static_folder="static", static_url_path="/static")

#只能於main使用，不能於blueprint文件使用
#解決json格式於api頁面中的中文解碼錯誤
app.config["JSON_AS_ASCII"]=False

app.secret_key="ImportantKey"#設定session的密鑰

@app.route("/")
def HomePage():
    if session.get("status") == None:
        session["status"]="未登入"
    return render_template("HomePage.html", Status=session.get("status"))

app.register_blueprint(app2)
app.register_blueprint(app3)
app.register_blueprint(app4)
app.register_blueprint(app5, url_prefix="/api")

if __name__ == "__main__":
    app.debug=True
    app.run(port=3000)