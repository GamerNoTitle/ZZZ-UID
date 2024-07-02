import cv2
import numpy as np
import pyautogui
import time
from datetime import datetime

# 加载模板图像
template1 = cv2.imread('img/image1.png', cv2.IMREAD_GRAYSCALE)
template2 = cv2.imread('img/image2.png', cv2.IMREAD_GRAYSCALE)
template3 = cv2.imread('img/image3.png', cv2.IMREAD_GRAYSCALE)

# 获取模板图像的尺寸
w1, h1 = template1.shape[::-1]
w2, h2 = template2.shape[::-1]
w3, h3 = template3.shape[::-1]

# 设置对应的坐标和匹配阈值
coordinates = {
    'image1.png': (960, 540),
    'image2.png': (700, 630),
    'image3.png': (960, 630)
}

thresholds = {
    'image1.png': 0.5,
    'image2.png': 0.8,
    'image3.png': 0.9
}

def match_and_click(template, coord, template_name, threshold):
    # 截屏
    screenshot = pyautogui.screenshot()
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    screenshot_gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)

    # 匹配模板
    result = cv2.matchTemplate(screenshot_gray, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    current_time = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    print(f"{current_time} Matching {template_name}: Max value = {max_val}")

    if max_val >= threshold:
        print(f"{current_time} Template {template_name} matched with a value of {max_val}. Clicking at {coord}.")
        
        # 计算匹配区域的中心点
        center_x = max_loc[0] + int(template.shape[1] / 2)
        center_y = max_loc[1] + int(template.shape[0] / 2)

        # 移动鼠标并点击
        pyautogui.moveTo(coord[0], coord[1])
        pyautogui.click()
        return True
    else:
        print(f"{current_time} Template {template_name} did not match. Max value: {max_val}")
        return False

# 主循环
while True:
    if match_and_click(template3, coordinates['image3.png'], 'image3.png', thresholds['image3.png']):
        # 暂停10秒
        current_time = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
        print(f"{current_time} Sleeping for 10 seconds.")
        time.sleep(10)
    
    match_and_click(template1, coordinates['image1.png'], 'image1.png', thresholds['image1.png'])
    time.sleep(0.5)  # 等待0.5秒，确保点击操作完成
    match_and_click(template2, coordinates['image2.png'], 'image2.png', thresholds['image2.png'])
    time.sleep(11.5)  # 等待11.5秒
