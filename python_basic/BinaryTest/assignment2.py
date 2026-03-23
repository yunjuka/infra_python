# assignment2.py

import tkinter as tk
from tkinter import messagebox


def clicked():
    if not input_value:
        return # 함수를 호출한 곳으로 실행의 흐름을 돌려준다(함수를 여기서 종료한다)

    try:
        # 0 과 1이 아니라면 함수 종료
        if not set(input_value).issubset({"0","1"}):
            result_label.config(text="0 과 1만 입력 가능", fg="red")
            return
        
        # 8 자리 이하가 아니라면 함수 종료
        if len(input_value) > 8:
            result_label.config(text="8 자리 까지만 입력 가능", fg="red")
            return
        
        # 2 진수 문자열을 10 진수 정수로 변환
        num = int(input_value,2)
        result_label.config(text=f"변환 결과: {num}")
        

    except Exception as e:
        label.config(text=f"숫자만 입력", fg="red")
        

if __name__ == '__main__':
    root = tk.Tk()
    root.title("과제2")
    root.geometry("400x200")
        
    # 레이블
    label = tk.Label(root, text="2진수 8자리를 10진수로 변환")
    label.pack(pady=20)

    # 입력창
    input_value = tk.Entry(root, font=("Arial", 12))
    input_value.pack(pady=5)
    input_value.focus()
        
    # 버튼
    btn = tk.Button(root, text="변환", command=clicked, width=10, bg="lightgrey")
    btn.pack(pady=15)

    # 결과
    result_label = tk.Label(root, text="변환 결과")
    result_label.pack(pady=20)

    root.mainloop()
