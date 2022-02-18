from flask import jsonify
from flask import request
from flask import session
from flask import Blueprint
import db

app5=Blueprint("api", __name__, static_folder="static", static_url_path="/api/static", template_folder="templates")

@app5.route("/members", methods=["GET"])
def api():
    conn=db.con_pool.get_connection()
    mycursor=conn.cursor()
    data={"data":{
        "id":None,
        "name":None,
        "username":None
    }}
    apiData=data["data"]
    account=request.args.get("username")
    check_account="SELECT * FROM member WHERE username=%s"
    ca=[account]
    mycursor.execute(check_account, ca)
    result=mycursor.fetchone()
    mycursor.close()
    if(result==None):
        data["data"]=None
        return jsonify(data)
    else:
        apiData["id"]=result[0]
        apiData["name"]=result[1]
        apiData["username"]=result[2]
        return jsonify(data)
    
@app5.route("/member", methods=["POST", "GET"])
def post_api():
    conn=db.con_pool.get_connection()
    mycursor=conn.cursor()
    name=request.get_json()
    account=session["account"]
    session["name"]=name["name"]
    Update_name="UPDATE member SET name=%s WHERE username=%s"
    mycursor.execute(Update_name, (name["name"], account, ))
    conn.commit()
    conn.close()
    if(account==None):
        data={
            "error":True
        }
    else:
        data={
            "ok":True
        }
    return jsonify(data)