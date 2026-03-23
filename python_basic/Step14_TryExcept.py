

from math import pi
from unittest import result


if __name__ == '__main__':
  
    try:
        num1:int = int(input("젯수 입력: "))
        num2:int = int(input("피젯수 입력: "))

        result = num1/num2
        print(f"{num1}를 {num2}로 나눈 결과 값: {result}")

    except Exception as e:
        print(f"에러 발생 {e}")
    else:
        pass
    finally:
        pass

print("종료")