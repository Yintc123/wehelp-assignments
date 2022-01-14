import json#利用json模組處理json資料
import csv
import urllib.request as req

def findtheFirstURL(strinfo, num):#num從1開始，由於num=0的字串為""
    strurl=""
    ad=[]
    for i in range(len(strinfo)):
        if (strinfo[i]=="h" and strinfo[i+1]=="t" and strinfo[i+2]=="t" and strinfo[i+3]=="p"):
            ad.append(strurl)#list.appenf(obj)：於list尾端增加新物件
        strurl+=strinfo[i]
    return ad[num]
def findtheFirstURL2(strinfo):#第二種方式找出第一個網址
    strurl=""
    n=strinfo.find("http",1)
    for i in range(n):
        strurl+=strinfo[i]   
    return strurl
def findAddress(strinfo):#找出地區
    n=strinfo.find("區")
    return strinfo[n-2]+strinfo[n-1]+strinfo[n]
            
url="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
with req.urlopen(url) as response:
    dataOri=json.load(response)
data=dataOri["result"]["results"]
with open("data.csv", mode="w", encoding="utf-8-sig") as file:
    #utf-8會有亂碼
    #UTF-8-Sig和UTF-8的主要差別是前者是UTF-8 with BOM (Byte Order Mark)
    file.write("項數,景點名稱,區域,經度,緯度,第一張圖片網址\n")
    i=0
    for row in data:
        file.write(str(i))
        file.write(","+row["stitle"])
        address=findAddress(row["address"])
        file.write(","+address)
        file.write(","+row["longitude"])
        file.write(","+row["latitude"])
        Surl=findtheFirstURL2(row["file"])
        file.write(","+Surl+"\n")
        #csv檔：","換欄；"\n"換行
        i+=1
        