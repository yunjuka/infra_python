# gui01.py

# tkinter import
import tkinter as tk

def clicked():
    # Entry(입력창)에 입력한 문자열 읽어오기
    name=name_entry.get()
    # label2 text 수정
    label2.config(text=f"입력 이름: {name}")


if __name__ == '__main__':

    root = tk.Tk()
    root.title("나의 App")
    root.geometry("400x200")

    # 레이블
    label = tk.Label(root, text="안녕하세요! python GUI입니다.")
    label.pack(pady=20)

    # 입력창
    name_entry = tk.Entry(root, font=("Arial", 12))
    name_entry.pack(pady=5)
    name_entry.focus()

    # 버튼
    btn = tk.Button(root, text="전송", command=clicked, width=10, bg="lightgrey")
    btn.pack(pady=15)

    label2 = tk.Label(root, text="결과...")
    label2.pack(pady=20)

    root.mainloop()