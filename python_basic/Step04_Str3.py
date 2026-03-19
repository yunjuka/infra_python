# yaml 형식 문자열 다루기

# yaml 문자열 다룰 때 외부 모듈을 pip으로 설치 후 import

import yaml


info = '''
name: 강윤주
addr: 부산
foods: 
  - 회
  - 곱창
isMan: false
body:
  weight: 80
  height: 176
'''

# info에 들어 있는 문자열을 dict type으로 바꾸기
result1 = yaml.safe_load(info)

# dict에 있는 내용 확인 후 다시 dict 을 yaml 문자열로 변경
result2 = yaml.dump(result1, sort_keys=False, allow_unicode=True)

print(type(result1))
print(type(result2))

print("종료")