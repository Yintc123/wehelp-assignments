from flask import request
from flask import render_template
from flask import Blueprint

app3=Blueprint("fail", __name__, static_folder="static", static_url_path="/fail/static", template_folder="templates")

@app3.route("/error/", methods=["GET"])
def fail():
    Fmessage=request.args.get("message")#將query stirng的訊息存至Fmessage
    return render_template("FailPage.html", FailMessage=Fmessage)