import cv2
import numpy as np
import pyautogui
import time
import ctypes
import sys
from datetime import datetime

welcome_msg = '''
 _______  _______  _______         _   _  _  ___   
(_____  )(_____  )(_____  )       ( ) ( )(_)(  _`\ 
     /'/'     /'/'     /'/'______ | | | || || | ) |
   /'/'     /'/'     /'/' (______)| | | || || | | )
 /'/'___  /'/'___  /'/'___        | (_) || || |_) |
(_______)(_______)(_______)       (_____)(_)(____/'

    https://github.com/GamerNoTitle/ZZZ-UID
    Telegram群组（有入群验证）：https://t.me/DohnaNyan
'''

# 检查是否以管理员权限运行
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

# 以管理员权限重新运行脚本
def run_as_admin():
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)

# 如果不是管理员，则重新以管理员权限运行脚本
if not is_admin():
    current_time = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    print(f"{current_time} 正在获取管理员权限……")
    run_as_admin()
    sys.exit()

# 调整模板图片大小
def resize_template(template, screen_width, screen_height):
    base_width, base_height = 1920, 1080
    scale_x = screen_width / base_width
    scale_y = screen_height / base_height
    new_width = int(template.shape[1] * scale_x)
    new_height = int(template.shape[0] * scale_y)
    resized_template = cv2.resize(template, (new_width, new_height))
    return resized_template

# 检测屏幕分辨率
screen_width, screen_height = pyautogui.size()

# 加载模板图像
template1 = resize_template(cv2.imread('img/image1.png', cv2.IMREAD_GRAYSCALE), screen_width, screen_height)
template2 = resize_template(cv2.imread('img/image2.png', cv2.IMREAD_GRAYSCALE), screen_width, screen_height)
template3 = resize_template(cv2.imread('img/image3.png', cv2.IMREAD_GRAYSCALE), screen_width, screen_height)
template4 = resize_template(cv2.imread('img/image4.png', cv2.IMREAD_GRAYSCALE), screen_width, screen_height)

# 获取模板图像的尺寸
w1, h1 = template1.shape[::-1]
w2, h2 = template2.shape[::-1]
w3, h3 = template3.shape[::-1]
w4, h4 = template4.shape[::-1]

# 设置对应的坐标和匹配阈值
coordinates = {
    'image1.png': (960, 540),
    'image2.png': (700, 630),
    'image3.png': (960, 630),
    'image4.png': (960, 630)
}

thresholds = {
    'image1.png': 0.5,
    'image2.png': 0.8,
    'image3.png': 0.9,
    'image4.png': 0.9
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
        # 按比例调整坐标
        adjusted_coord = adjust_coordinates(coord)
        print(f"{current_time} 当前页面成功以最大匹配相似度 {max_val} 匹配上了 {template_name}，正在点击位置 {adjusted_coord}")
        # 移动鼠标并点击
        pyautogui.moveTo(adjusted_coord[0], adjusted_coord[1])
        pyautogui.click()
        return True
    else:
        print(f"{current_time} 当前页面看起来不像 {template_name}，最大匹配相似度为 {max_val}")
        return False

# 按比例调整坐标
def adjust_coordinates(coord):
    base_width, base_height = 1920, 1080
    adjusted_x = int(coord[0] * screen_width / base_width)
    adjusted_y = int(coord[1] * screen_height / base_height)
    return (adjusted_x, adjusted_y)

if __name__ == '__main__':
    # 欢迎信息
    print(welcome_msg)
    current_time = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    print(f"{current_time} 检测到屏幕分辨率: {screen_width}x{screen_height}")
    if screen_width/screen_height != 1920/1080:
        current_time = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
        print(f'{current_time} 不支持当前分辨率：{screen_width}x{screen_height}！请使用16:9的分辨率再打开本程序！')
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
        time.sleep(6.6)  # 等待6.6秒
        if match_and_click(template4, coordinates['image4.png'], '网络超时提示', thresholds['image4.png']):
            current_time = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
            print(f"{current_time} 检测到出现网络问题，请保持网络通畅！")
