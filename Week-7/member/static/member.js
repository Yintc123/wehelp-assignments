function searchName(){
    let account=document.getElementById("search").value;
    let text=document.getElementById("name");
    url=url_for_check+account;
    fetch(url).then(response => {
        return response.json();
    }).then(data => {
        result=data["data"]
        if(result==null){
            console.log(result);
            text.style.color="red";
            text.textContent="找不到此使用者";
        }else{
            console.log(result);
            text.style.color="blue";
            text.textContent=result["name"]+"("+result["username"]+")";
        }
    })
    
}

function renewName(){
    let name=document.getElementById("inputName").value;
    let message=document.getElementById("message");
    let n=document.getElementById("n");
    if(name==""){
        message.style.color="red";
        message.textContent="請輸入姓名";
    }else{
        data={
            "name":name
        }
        fetch(
            url_for_renewName,{
                body:JSON.stringify(data),
                headers:{
                    "content-type":"application/json"
                },
                method:"POST"
            }
        ).then(response => {
            return response.json();
        }).then(response => {
            console.log(response);
            if(response["ok"]==true){
                n.textContent=name;
                message.style.color="blue";
                message.textContent="更新成功!";
            }else{
                message.style.color="red";
                message.textContent="更新失敗~";
            }
        }
        )
    }
}

url_for_check="http://127.0.0.1:3000/api/members?username=";
url_for_renewName="http://127.0.0.1:3000/api/member";
console.log("hi");
ok={
    "ok":true
}
error={
    "error":true
}