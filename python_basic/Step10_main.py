'''
    현재 파일, 즉 Step10_main.py 에서 run 실행하면

    __name__ 은 "__main__" 이라는 문자열이 들어온다.
    
    따라서  __name__ 을 확인해하면 해당 파일이 main 으로 실행되었는지 여부 확인 가능
    
    다른 곳에서 import 했을 때 실행되지 않는 코드 블럭을 만들 때 사용함
'''

print("Step10_main.py 가 실행됨")
print(__name__)

class TestClass:
    pass

# 아래 if문은 main 으로 실행 시에만 실행 됨 (다른 곳에서 import 시 실행X)
if __name__ == "__main__":
    print("시작")
    print("작업")
    print("종료")