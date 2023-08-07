import os
import requests
import openpyxl
import tkinter as tk
from tkinter import filedialog


def on_button1_click():
    print("开始任务被点击")


def on_button2_click():
    print("停止任务被点击")


window = tk.Tk()
window.title("直链提取进程")
# 设置窗体大小
window.minsize(275, 100)

# 锁定窗体大小，使其不可缩放
window.resizable(False, False)

button1 = tk.Button(window, text="开始", command=on_button1_click)
button1.pack(padx=20, pady=10)

button2 = tk.Button(window, text="停止", command=on_button2_click)
button2.pack(padx=20, pady=10)

window.mainloop()
