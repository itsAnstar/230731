import pandas as pd
import pyautogui
import tkinter as tk
from tkinter import filedialog
from pynput import mouse, keyboard
import time

# 保存需要自动点击的坐标的列表
selected_coordinates = []

# 保存按钮点击的坐标的列表
button_click_coordinates = []

# 记录下一个鼠标点击坐标在selected_coordinates中的索引
next_click_index = 0

# 函数用于模拟键盘复制和粘贴快捷键
def simulate_copy_paste():
    pyautogui.hotkey('ctrl', 'c')  # 复制
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'v')  # 粘贴
    time.sleep(1)

# 函数用于模拟鼠标点击
def simulate_mouse_click(x, y):
    pyautogui.click(x, y, duration=0.5)

# 函数用于创建窗体并添加按钮和标签
def create_window():
    window = tk.Toplevel()
    window.title("选择自动点击坐标")
    window.attributes('-topmost', True)  # 窗口保持最前

    # 设置窗体默认最小宽度为400
    window.minsize(400, 1)

    # 创建按钮和标签并绑定事件处理函数
    for i in range(5):
        button_text = str(i + 1)
        button = tk.Button(window, text=button_text, command=lambda btn_text=button_text: on_button_click(btn_text))
        button.grid(row=i, column=0, padx=5, pady=5)

        label = tk.Label(window, text="", anchor="w")
        label.grid(row=i, column=1, padx=5, pady=5)

        labels.append(label)

    # 创建选择文件按钮
    file_button = tk.Button(window, text="选择Excel文件", command=select_file)
    file_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

    window.mainloop()

# 事件处理函数，保存选中的坐标
def on_button_click(button_text):
    global selected_coordinates, next_click_index
    selected_coordinates.append(button_text)
    update_labels()
    next_click_index = len(selected_coordinates)  # 更新下一个鼠标点击坐标的索引
    listen_next_click()

# 更新标签显示内容
def update_labels():
    global selected_coordinates
    for i in range(5):
        if i < len(selected_coordinates):
            label_text = f"选中的点击坐标：{selected_coordinates[i]}"
        else:
            label_text = ""
        labels[i].config(text=label_text)

# 事件处理函数，选择Excel文件
def select_file():
    global selected_coordinates
    file_path = filedialog.askopenfilename(filetypes=[("Excel Files", "*.xlsx")])
    if file_path:
        df = pd.read_excel(file_path, sheet_name="合作带货视频")
        create_window()

# 函数用于监听鼠标点击事件
def on_click(x, y, button, pressed):
    global button_click_coordinates
    if pressed:
        button_click_coordinates.append((x, y))

# 函数用于监听键盘事件
def on_press(key):
    try:
        # 检测Shift + 空格的组合键
        if key == keyboard.Key.shift_r or key == keyboard.KeyCode.from_char(' '):
            # 开始自动点击
            start_auto_clicking()
            # 停止键盘监听
            return False
    except AttributeError:
        pass

# 开始监听下一个鼠标点击
def listen_next_click():
    with mouse.Listener(on_click=on_next_click) as listener:
        listener.join()

# 处理下一个鼠标点击事件
def on_next_click(x, y, button, pressed):
    global next_click_index, selected_coordinates
    if pressed and next_click_index < len(selected_coordinates):
        selected_coordinates[next_click_index] = f"x: {x}, y: {y}"
        update_labels()
        next_click_index += 1

# 开始自动点击
def start_auto_clicking():
    global selected_coordinates, button_click_coordinates
    # 获取按钮点击的坐标
    button_click_coordinates = button_click_coordinates[:len(selected_coordinates)]
    # 点击选中的坐标地址
    for click_x, click_y in button_click_coordinates:
        simulate_mouse_click(click_x, click_y)
        time.sleep(1)

    # 监听键盘直到按下Shift加空格后继续点击选中的坐标
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

    # 模拟键盘快捷键粘贴，粘贴内容至与第一步对应的第4列同一行
    pyautogui.typewrite(row['发布时间'] + row['发布作者名称'])
    simulate_copy_paste()

    # 点击两个选中的坐标
    simulate_mouse_click(x3, y3)
    time.sleep(1)
    simulate_mouse_click(x4, y4)
    time.sleep(1)

# 声明空的标签列表
labels = []

# 主函数
def main():
    select_file()

if __name__ == "__main__":
    main()
