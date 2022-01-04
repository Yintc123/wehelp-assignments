#第一題
print("第一題：")
def calculate(min, max):
    result=0
    for i in range(min, max+1):
        result+=i
    print(str(min)+"+...+"+str(max)+"="+str(result)) 
    return result

calculate(1, 3)
calculate(4, 8)
print("-----------我是分隔線----------")
#第二題
print("第二題：")
def avg(data):
    sum=0
    employees=data["employees"]
    for i in employees:
        sum+=i["salary"]
    print("平均："+str(sum/data["count"]))
    return sum/data["count"]

avg({
    "count":3,
    "employees":[
        {
            "name":"John",
            "salary":30000
        },
        {
            "name":"Bob",
            "salary":60000
        },
        {
            "name":"Jenny",
            "salary":50000
        }
    ]
})
print("-----------我是分隔線----------")
#第三題
print("第三題：")
def maxProduct(nums):
    n1=nums[0]*nums[1]
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if(nums[j]*nums[i]>n1):
                n1=nums[j]*nums[i]
    print("兩數相乘最大的值為："+str(n1))    
    return n1

maxProduct([5, 20, 2, 6]) # 得到 120
maxProduct([10, -20, 0, 3]) # 得到 30
maxProduct([-1, 2]) # 得到 -2
maxProduct([-1, 0, 2]) # 得到 0
maxProduct([-1,-2,0]) # 得到 2
print("-----------我是分隔線----------")
#第四題
print("第四題：")
def twoSum(nums, target):
    n1=-1
    n2=-1
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if(nums[i]+nums[j]==target):
                n1=i
                n2=j
                break;
    return [n1, n2]

result=twoSum([2, 11, 7, 15], 9)
print(result)
print("-----------我是分隔線----------")
#第五題
print("第五題：")
def maxZeros(nums):
    n1=0
    n2=0
    for i in range(len(nums)):
        if(nums[i]==0):
            n1+=1
            if(n1>n2):
                n2=n1
        else:
            n1=0
    print("連續"+str(n2)+"個0")
    return n2
maxZeros([0, 1, 0, 0]) # 得到 2
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]) # 得到 4
maxZeros([1, 1, 1, 1, 1]) # 得到 0
maxZeros([0, 0, 0, 1, 1]) # 得到 3