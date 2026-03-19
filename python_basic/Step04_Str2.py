import json
from unittest import result

info = '''{
    "name":"강윤주",
    "addr":"부산",
    "foods":["물고기","곱창"]
}'''

result = json.loads(info)\

print(result["name"])
print(result["addr"])
print(result["foods"])
print(result["foods"][0])
print(result["foods"][1])

result2 = json.dumps(result)

print(result2)
print("종료")