
'''
class MyCar:
    def __init__(self, name:str):
        print("생성자가 호출됨")
        print(self)

        self.name = name

    def drive(self):
        print(f"{self.name}가 달림") 

if __name__ == '__main__':
  c1: MyCar = MyCar("소나타")
  c1.drive()
'''

class Car:                             # 설계도
    def __init__(self, brand, color):   # 설계도 내용
        self.brand = brand
        self.color = color
    def drive(self):        # 설계도 속 기능
        print(f"{self.brand}, {self.color} 자동차")

if __name__ == "__main__":
    c1 = Car("소나타", "흰색")          # 객체 생성, 객체에 변수 담기
    c1.drive()                        # 변수의 설계도 속 기능 호출