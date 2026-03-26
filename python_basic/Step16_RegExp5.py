# Step16_RegExp5.py

import re


if __name__ == '__main__':
  input_id = input("아이디 입력(영문자로 시작하고, 5-10글자 이내, 특수문자 허용안함): ")

  # 위 조건에 맞으면 '가입' 아니면 '사용 안됨'

  pattern = r"^[a-zA-Z][a-zA-Z0-9]{4,9}$"
  if re.search(pattern, input_id):
    print("가입")
  else:
    print("불가")