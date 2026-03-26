# Step16_RegExp4.py

import re


if __name__ == '__main__':
    user_id = input("아이디 입력(영 대소문자, 숫자만 가능): ")

    # 입력한 문자열을 검증해서 조건에 맞으면 '가입' 아니면 '사용 안됨'

    pattern = r"^[a-zA-Z0-9]+$"

    if re.search(pattern, user_id):
        print("가입 완료")
    else:
        print("사용 안됨")