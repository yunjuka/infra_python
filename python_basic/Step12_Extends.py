# Step12_Extends.py


# 클래스 상속에 대해서 알아보자


# 가상의 전화기를 찍어낼 클래스
class Phone:
    def call(self):
        print("전화를 걸어요!")


# 가상의 핸드폰을 찍어낼 클래스 , Phone 클래스를 extends 해서 정의한다
class HandPhone(Phone): # 클래스명(상속받을 클래스)
    def mobile_call(self):
        print("이동중에 전화를 걸어요!")


    def take_picture(self):
        print("100만 화소의 사진을 찍어요!")


if __name__ == "__main__" :
    p1:Phone = Phone()
    p1.call()


    print("-------------------")


    p2:HandPhone = HandPhone()
    p2.call()
    p2.mobile_call()
    p2.take_picture()


