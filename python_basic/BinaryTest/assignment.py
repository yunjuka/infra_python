# assignment.py

# 10 진수 숫자를 입력하고 전송을 누르면 아래 label에 출력
# 10 진수 숫자를 입력하고 전송을 누르면 아래 label에 2진수로
# 10 진수 숫자를 입력하고 전송을 누르면 2진수 8자리로
# 0-255 사이값이 아니면 경고 알림

import tkinter as tk

root = tk.Tk()

root.title("과제")

root.geometry("400x400")

# 레이블
label = tk.Label(root, text="0~255 값을 입력")
label.pack(pady=20)

# 입력창
num_entry = tk.Entry(root, font=("Arial", 12))
num_entry.pack(pady=5)
num_entry.focus()

def clicked():
    try:  
        # Entry(입력창)에 입력한 문자열 읽어오기
        num=int(num_entry.get())

        if 0 <= num <= 255:
            # label2 text 수정
            label2.config(text=f"입력 십진수: {num}")  
            # label3 text 수정
            binary_num = bin(num)
            label3.config(text=f"이진수로 변환 결과: {binary_num[2:]}")
            # label4 text 수정
            label4.config(text=f"이진수로 변환 결과: {num:08b}")
        else:
            label.config(text=f"0~255 사이 값을 입력하시오", fg="red")  

    except Exception as e:
        label.config(text=f"입력 값을 다시 확인하시오", fg="red")  


# 버튼
btn = tk.Button(root, text="전송", command=clicked, width=10, bg="lightgrey")
btn.pack(pady=15)

# 십진수
label2 = tk.Label(root, text="결과")
label2.pack(pady=20)

# 이진수
label3 = tk.Label(root, text="...")
label3.pack(pady=20)

# 이진수 8자리
label4 = tk.Label(root, text="...")
label4.pack(pady=20)

root.mainloop()