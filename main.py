import cv2
import numpy as np
import pyautogui
import time
from datetime import datetime

welcome_msg = '''
 _______  _______  _______         _   _  _  ___   
(_____  )(_____  )(_____  )       ( ) ( )(_)(  _`\ 
     /'/'     /'/'     /'/'______ | | | || || | ) |
   /'/'     /'/'     /'/' (______)| | | || || | | )
 /'/'___  /'/'___  /'/'___        | (_) || || |_) |
(_______)(_______)(_______)       (_____)(_)(____/'

       https://github.com/GamerNoTitle/ZZZ-UID
'''

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
    print(f"{current_time} 正在尝试匹配 {template_name}，最大匹配相似度 = {max_val}")

    if max_val >= threshold:
        print(f"{current_time} 当前页面成功以最大匹配相似度 {max_val} 匹配上了 {template_name}，正在点击位置 {coord}")
        
        # 移动鼠标并点击
        pyautogui.moveTo(coord[0], coord[1])
        pyautogui.click()
        return True
    else:
        print(f"{current_time} 当前页面看起来不像 {template_name}，最大匹配相似度为 {max_val}")
        return False

print(welcome_msg)

# 主循环
while True:
    if match_and_click(template3, coordinates['image3.png'], '风控页面', thresholds['image3.png']):
        # 暂停15秒
        current_time = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
        print(f"{current_time} 检测到被风控！休眠15秒")
        time.sleep(15)
    
    match_and_click(template1, coordinates['image1.png'], '登录主页面', thresholds['image1.png'])
    time.sleep(1)  # 等待1秒，确保点击操作完成
    match_and_click(template2, coordinates['image2.png'], '维护提示', thresholds['image2.png'])
    time.sleep(6.5)  # 等待6.5秒
