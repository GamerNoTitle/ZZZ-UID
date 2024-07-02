# ZZZ-UID

只是一个帮我抢UID的小程序罢了

> [!Warning]
>
> 一定一定一定要以管理员身份打开程序，要不然点不下去！！！

## 使用要求

- 需要Python环境，版本没有什么特定的要求，我用的是`Python 3.11.9`
- 稳定的网络环境
- ZZZ客户端（要求设置为简体中文，不是简体中文有可能会识别不出来，分辨率为**1920*1080全屏**）

## 开始使用

Step 1. 首先打开终端，安装我们需要的轮子

```powershell
pip install -r requirements.txt
```

然后，以**管理员身份**打开终端，运行本程序

```powershell
python main.py
```

放着就好了，程序设置为每分钟点击5次，每次间隔12秒（因为在做这个东西的时候发现跟崩铁不一样，米忽悠这次加了风控，个人测下来大概是`5次/分钟`，所以设置的是12秒，如果要修改请自己改主循环里面的时间

```python
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
```

**不建议修改第一个`time.sleep(0.5)`，点击后需要这个时间来弹出提示窗口**
