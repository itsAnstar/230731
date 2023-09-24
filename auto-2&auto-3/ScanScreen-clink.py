import tkinter as tk
from tkinter import ttk
import pyautogui
import cv2
import numpy as np
import time


def take_screenshot_and_recognize():
    try:
        # 截取屏幕并保存图片至程序根目录
        screenshot = pyautogui.screenshot()
        screenshot.save("screenshot.png")
        print("截图已保存")

        # 识别窗口
        window_width = 518
        window_height = 975

        screenshot = cv2.imread("screenshot.png")

        template_image = cv2.imread("template.png", cv2.IMREAD_COLOR)
        button_image = cv2.imread("2button.png", cv2.IMREAD_COLOR)

        if template_image is not None and button_image is not None:
            result = cv2.matchTemplate(screenshot, template_image, cv2.TM_CCOEFF_NORMED)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

            threshold = 0.8

            if max_val >= threshold:
                left_top = max_loc
                right_top = (left_top[0] + window_width, left_top[1])
                left_bottom = (left_top[0], left_top[1] + window_height)
                right_bottom = (left_top[0] + window_width, left_top[1] + window_height)

                print("识别成功")
                print("左上角坐标:", left_top)
                print("右上角坐标:", right_top)
                print("左下角坐标:", left_bottom)
                print("右下角坐标:", right_bottom)

                # 计算点击位置的右下角坐标
                click_x = left_top[0] + 250
                click_y = left_top[1] + 270

                # 模拟鼠标点击
                pyautogui.click(click_x, click_y)

                print("在坐标({}, {})上进行了一次点击".format(click_x, click_y))

                # 睡眠3秒钟
                time.sleep(3)

                # 进行第二次识别
                result2 = cv2.matchTemplate(screenshot, button_image, cv2.TM_CCOEFF_NORMED)
                min_val2, max_val2, min_loc2, max_loc2 = cv2.minMaxLoc(result2)
                threshold2 = 0.8

                if max_val2 >= threshold2:
                    button_left_top = max_loc2
                    button_right_top = (button_left_top[0] + button_image.shape[1], button_left_top[1])
                    button_left_bottom = (button_left_top[0], button_left_top[1] + button_image.shape[0])
                    button_right_bottom = (
                    button_left_top[0] + button_image.shape[1], button_left_top[1] + button_image.shape[0])

                    # 计算并点击右侧中间位置
                    click_x2 = button_left_top[0] + (button_right_top[0] - button_left_top[0]) // 2
                    click_y2 = button_left_top[1] + (button_left_bottom[1] - button_left_top[1]) // 2

                    # 模拟鼠标点击
                    pyautogui.click(click_x2, click_y2)
                    print("在坐标({}, {})上进行了一次点击".format(click_x2, click_y2))

                else:
                    print("未找到匹配的第二个按钮")

            else:
                print("未找到匹配窗口")
        else:
            print("无法加载模板图像")
    except Exception as e:
        print(f"发生错误: {str(e)}")


# 创建主窗口
root = tk.Tk()
root.title("截图和识别窗口")

# 创建按钮
button = ttk.Button(root, text="截取屏幕并识别窗口", command=take_screenshot_and_recognize)
button.pack(pady=20)

# 运行主循环
root.mainloop()
