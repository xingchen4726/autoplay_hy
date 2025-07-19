import pyautogui
import pyperclip
import pyscreeze
import time
import sys
from pynput import keyboard

# 定义K值，控制循环次数
# 添加H键退出标志
h_pressed = False

def on_press(key):
    global h_pressed
    try:
        if key.char == 'h' or key.char == 'H':
            h_pressed = True
    except AttributeError:
        pass
    except Exception as e:
        print(f"键盘监听错误: {e}")

# 创建键盘监听器
try:
    listener = keyboard.Listener(on_press=on_press)
    listener.start()
except Exception as e:
    print(f"无法启动键盘监听: {e}")
    sys.exit(1)
K = 0
run = 0
# 设置置信度阈值（可选，根据实际情况调整）
confidence_threshold = 0.8     #图片相似度
tolerance = 20     # 设置颜色容差（可选，默认为0）
target_color = (188, 101, 219)  # 示例：紫色



# 等待几秒以切换到微信小程序界面
print("脚本开始运行，请在5秒内切换到游戏界面")
print("按H键可退出循环")
time.sleep(5)


# 获取当前屏幕分辨率
screen_width, screen_height = pyautogui.size()
print(f"屏幕分辨率: {screen_width}x{screen_height}")


# 大循环
try:
    while not h_pressed:
        try:
            pyautogui.click(524,560)
            time.sleep(0.5)  # 添加0.5秒间隔
            pyautogui.click(524,746)
            time.sleep(0.5)  # 添加0.5秒间隔
            pyautogui.click(524,939)
            time.sleep(0.5)  # 添加0.5秒间隔
        except Exception as e:
            print(f"点击操作出错: {e}")
            time.sleep(1)
finally:
    listener.stop()
    print("脚本已停止")

    

