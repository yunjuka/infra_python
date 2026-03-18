'''
1. 순서가 있다
2. 여러 type 가능
3. 값 변경 가능
'''

num = [10,20,30]
dates = [10,'xxx',True]

num.append(40)
num_len = len(num)

names = ['김구라', '해골']

# 인덱스로 인한 참조
name0 = names[0]

# 인덱스를 이용한 삭제
del names[0]

# 마지막 index 삭제 후 가져오기
result = num.pop()

print("finish")