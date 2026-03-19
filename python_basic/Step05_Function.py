#Step05_Function.py

from unittest import result


def test(arg):
    print("전달 내용",arg)
    print(f"전달 내용 {arg}")

test(10)
test("kim")


def print_sum(num1:int, num2:int):
    sum = num1+num2
    print(f"{num1} + {num2} = {sum}")

print_sum(10,20)


def print_info(name:str, addr:str):
    print(f"이름은 {name} 주소는 {addr}")

print_info("김구라", "노량진")
print_info(addr="행신", name="해골")


def get_sum(num1:int, num2:int):
    sum = num1 + num2
    return sum

result = get_sum(10,.20)

print("종료")
