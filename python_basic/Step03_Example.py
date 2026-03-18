
# 3명의 회원정보를 각각 dict에 담고 list에 담기

num1 = {"name":"Kim", "number":1, "addr":"서울"}
num2 = {"name":"Park", "number":2, "addr":"부산"} 
num3 = {"name":"Kang", "number":3, "addr":"용인"}

members = [num1, num2, num3]

print(members)

a = members
b = members[0]
c = members[0]["name"]
d = members[0]["number"]


print("종료")
