
nums = [10,20,30,40,50]
names = ['Kim', 'Park', 'Oh']

# nums에 저장되어 있는 데이터를 순서대로 참조하며 출력
for i in nums:
    print(i)

# names에 있는 데이터를 앞에서부터 참조하며 출력
for i in names:
    print("names를 순서대로 출력")
    print(i)

r = range(5)
print(r)

for i in range(5):
    print(i)

for i in range(len(names)):
    print(i,names[i])