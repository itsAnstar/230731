import pandas as pd
import pyautogui
import tkinter as tk
from pynput import keyboard

# 保存需要自动点击的坐标的列表
selected_coordinates = []

# 函数用于模拟键盘复制和粘贴快捷键
def simulate_copy_paste():
    pyautogui.hotkey('ctrl', 'c')  # 复制
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'v')  # 粘贴
    time.sleep(1)

# 函数用于监听键盘事件
def on_press(key):
    try:
        # 检测Shift + 空格的组合键
        if key == keyboard.Key.shift_r or key == keyboard.KeyCode.from_char(' '):
            # 停止监听
            return False
    except AttributeError:
        pass

# 函数用于模拟鼠标点击
def simulate_mouse_click(x, y):
    pyautogui.click(x, y, duration=0.5)

# 函数用于创建窗体并添加按钮
def create_window(num_buttons):
    window = tk.Tk()
    window.title("选择自动点击坐标")
    
    # 创建按钮并绑定事件处理函数
    for i in range(num_buttons):
        button_text = str(i + 1)
        button = tk.Button(window, text=button_text, command=lambda btn_text=button_text: on_button_click(btn_text))
        button.pack()

    window.mainloop()

# 事件处理函数，保存选中的坐标
def on_button_click(button_text):
    global selected_coordinates
    selected_coordinates.append(button_text)

# 主函数
def main():
    file_path = 'your_excel_file.xlsx'
    df = pd.read_excel(file_path)

    # 根据需要选中的坐标数量创建窗体并添加按钮
    num_buttons = df.shape[0]
    create_window(num_buttons)

    # 使用选中的坐标进行自动点击
    for index, row in df.iterrows():
        if str(index + 1) in selected_coordinates:
            url = row['视频URL地址'][1:]

            # 模拟键盘复制快捷键复制内容
            pyautogui.typewrite(url)
            simulate_copy_paste()

            # 点击选中的坐标地址第一次
            simulate_mouse_click(x1, y1)
            time.sleep(1)

            # 点击选中的坐标地址第二次
            simulate_mouse_click(x2, y2)
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

if __name__ == "__main__":
    main()
