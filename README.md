# ZZZ-UID

只是一个帮我抢UID的小程序罢了；**禁止用于违法目的！！！**

Telegram群组（有入群验证）：https://t.me/DohnaNyan

> [!CAUTION]
> 
> **因为STAR来得太快了，在这里强调一点：禁止宣传！！！否则删库跑路！！！**

> [!IMPORTANT]
>
> **本程序是按照崩铁那个时候的逻辑来做的，即进入游戏就分配UID，如果ZZZ要创角（即输入名字选择性别后）才分配UID的话我是无能为力的**
>
> 一定要采用1080p分辨率或者其他16:9分辨率（未测试，理论上可行，不行自己调点击的位置）并全屏游戏，并且需要把游戏放在前台置顶窗口
>
> 可以多屏，但是你的主屏幕一定要是16:9的

> [!Warning]
>
> 一定一定一定要以管理员身份打开程序，要不然点不下去！！！
> 
> 当你打开本程序的时候，默认你同意：①承诺合法使用本程序 ②抢的是自己的号 ③并非用于商业行为
> 
> 使用本程序造成的一切后果自行承担，开发者不背锅

## 使用要求

- 需要Python环境，版本没有什么特定的要求，我用的是`Python 3.11.9`（没有Python环境直接下载RELEASE，非必要不要用Pre-Release）
- 稳定的网络环境
- ZZZ客户端（要求设置为简体中文，不是简体中文有可能会识别不出来，分辨率为**1920*1080全屏**或者任意16:9分辨率，但是一定要全屏！！！**仅在1080p分辨率下通过测试，其他分辨率理论上应该可以用的**）

## 开始使用

Step 1. 首先打开终端，安装我们需要的轮子

```powershell
pip install -r requirements.txt
```

然后，以**管理员身份**打开终端，运行本程序

```powershell
python main.py
```

放着就好了，经过测试，每7.5秒一循环为米忽悠设置的极限，本程序设置的为7.6秒一循环，避免压线；如果仍然触发了风控，会暂停15秒，如果需要更高的频率，请在下面这段代码自己修改

```python
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
```

**不建议修改第一个`time.sleep(1)`，点击后需要这个时间来弹出提示窗口**

