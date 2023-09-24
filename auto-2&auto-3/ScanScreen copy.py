import tkinter as tk
from tkinter import ttk
import pyautogui
import cv2
import numpy as np


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

        if template_image is not None:
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

                # 裁切识别到的窗口范围
                cropped_image = screenshot[left_top[1]:left_top[1] + window_height,
                                left_top[0]:left_top[0] + window_width]

                # 显示裁切后的图像
                cv2.imshow("check positioning", cropped_image)
                cv2.waitKey(0)
                cv2.destroyAllWindows()

            else:
                print("未找到匹配窗口")
        else:
            print("无法加载模板图像")
    except Exception as e:
        print(f"发生错误: {str(e)}")


# 创建主窗口
root = tk.Tk()
root.title("截图和识别窗口")
# 设置窗口大小为
root.geometry("350x100")

# 创建按钮
button = ttk.Button(root, text="截取屏幕并识别窗口", command=take_screenshot_and_recognize)
button.pack(pady=20)

# 运行主循环
root.mainloop()
