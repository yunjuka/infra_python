# 다중 if 문 구성

disk_usage = int(input("사용률 입력(0-100): "))

if disk_usage >= 90:
    print("용량 부족")
elif disk_usage >= 70:
    print("보통")
else:
    print("넉넉")