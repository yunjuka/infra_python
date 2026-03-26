# Step16_RegExp3.py

from logging import info
import re


logs = [
    "[INFO] Server started successfully.",
    "[WARN] Memory usage is high.",
    "[ERROR] Database connection failed.",
    "[DEBUG] x = 10"
]

# logs에서 ERROR or WARN 로그만 찾아서 콘솔창에 출력
for log in logs:
    if re.search(r'WARN|ERROR', log):
        print(log)


# logs에서 INFO 를 찾아 문구 변경 후 출력
for log in logs:
    if re.search(r'INFO',log):
        new_log = re.sub(r'INFO', "INFORMATION", log)
        print(new_log)

# 위와 같이 바꾸는데 다른 것들도 출력함
for log in logs:
    new_log = re.sub(r'INFO', 'INFOMATION', log)
    print(new_log)


# [WARN] 또는 [ERROR] 로 문자열이 시작하는지 검증할 정규 표현식

for log in logs:
    if re.search(r"^\[WARN\]",log):
        print(log)