#tuple

tuple1: tuple = ("one", "two", "three")

tuple2 = 10,20,30
tuple3 = "hello", "world"

a, b, c = tuple2

first = "girl"
second = "boy"

tmp = first
first = second
first = tmp

first, second = second, first
print("종료")