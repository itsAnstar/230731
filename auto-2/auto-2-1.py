import tkinter as tk

def on_button1_click():
    print("开始任务被点击")

def on_button2_click():
    print("停止任务被点击")

window = tk.Tk()
window.title("直链提取进程")

button1 = tk.Button(window, text="开始", command=on_button1_click)
button1.pack(padx=20, pady=10)

button2 = tk.Button(window, text="停止", command=on_button2_click)
button2.pack(padx=20, pady=10)

window.mainloop()
