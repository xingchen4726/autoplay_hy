# 使用电脑模拟器实现脚本
import pyautogui
import pyperclip
import pyscreeze
import time

# 定义K值，控制循环次数
K = 0
run = 0
# 设置置信度阈值（可选，根据实际情况调整）
confidence_threshold = 0.8     #图片相似度
tolerance = 20     # 设置颜色容差（可选，默认为0）
target_color = (188, 101, 219)  # 示例：紫色

def end():
    while True:
        try:
            # 尝试找到退出图像
            endlocation = pyautogui.locateOnScreen('end2.png', confidence=confidence_threshold)
            if endlocation:
                print("退出图像找到，位置：", endlocation)
                # 如果识别到continue图片，点击其中心位置
                end_center = pyscreeze.center(endlocation)
                pyautogui.click(end_center)
                print("退出对局")
                pyautogui.click(1500, 900)
                pyautogui.click(1500, 900)
                pyautogui.click(1500, 900)
                pyautogui.click(1500, 900)
                pyautogui.click(1500, 900)
                time.sleep(4)
                pyautogui.click(1500, 900)
                pyautogui.click(1500, 900)
                pyautogui.click(1500, 900)
                pyautogui.click(1500, 900)
                pyautogui.click(1500, 900)
                time.sleep(4)
                pyautogui.click(1500, 900)
                pyautogui.click(1500, 900)
                pyautogui.click(1500, 900)
                pyautogui.click(1500, 900)
                pyautogui.click(1500, 900)
                time.sleep(4)
                pyautogui.click(1500, 900)
                pyautogui.click(1500, 900)
                pyautogui.click(1500, 900)
                pyautogui.click(1500, 900)
                pyautogui.click(1500, 900)
                time.sleep(4)
                pyautogui.click(1500, 900)
                return
            else:
                print("退出图像未找到")
                time.sleep(2)
        except pyautogui.ImageNotFoundException:
            print("退出图像未找到，继续运行程序")
            time.sleep(2)
            # 在这里可以添加找不到图片时的处理逻辑
        except Exception as e:
            print("其他错误：", e)
            time.sleep(2)
def check_and_move(x_target, y_target, x_move, y_move, direction):
    # pyautogui.moveTo(x_target, y_target, duration=0.2)
    # if pyscreeze.pixelMatchesColor(x_target, y_target, target_color, tolerance):
    print("颜色匹配成功")
    pyautogui.moveTo(x_move, y_move, duration=0.2)
    if direction == "up":
        pyautogui.dragTo(x_move, y_move - 100, duration=0.6, button='left')
    elif direction == "down":
        pyautogui.dragTo(x_move, y_move + 100, duration=0.6, button='left')
    elif direction == "left":
        pyautogui.dragTo(x_move - 100, y_move, duration=0.6, button='left')
    elif direction == "right":
        pyautogui.dragTo(x_move + 100, y_move, duration=0.6, button='left')
    # else:
        # print("颜色匹配失败")


def run():
    while True:
        

        # 使用函数简化代码
        check_and_move(1100, 500, 400, 900, "down")
        
        check_and_move(1300, 700, 400, 900, "left")
        check_and_move(1100, 900, 400, 900, "up")
        check_and_move(900, 700, 400, 900, "right")
        # 点击屏幕右侧
        pyautogui.click(1500, 900)  # 点击屏幕右侧的(1000, 500)位置
        pyautogui.click(1500, 900) 
        pyautogui.click(1500, 900) 
        print("控制开火")
        
        # 每次操作后等待6秒
        time.sleep(2)
        try:
            # 尝试找到继续图像
            continuelocation = pyautogui.locateOnScreen('continue2.png', confidence=confidence_threshold)
            if continuelocation:
                print("继续图像找到，位置：", continuelocation)
                # 如果识别到continue图片，点击其中心位置
                continue_center = pyscreeze.center(continuelocation)
                pyautogui.click(continue_center)
                print("点击继续")
                time.sleep(2)
                # pyautogui.click(continue_center)
                time.sleep(2)
                end()
                return
            else:
                print("继续图像未找到")
        except pyautogui.ImageNotFoundException:
            print("继续图像未找到，继续运行程序")
            # 在这里可以添加找不到图片时的处理逻辑
        except Exception as e:
            print("其他错误：", e)


# 等待几秒以切换到微信小程序界面
print("脚本开始运行，请在5秒内切换到游戏界面")
time.sleep(5)


# 获取当前屏幕分辨率
screen_width, screen_height = pyautogui.size()
print(f"屏幕分辨率: {screen_width}x{screen_height}")


# 大循环
while  K<20:
    try:
        # 尝试找到开始图像
        startlocation = pyautogui.locateOnScreen('start2.png', confidence=confidence_threshold)
        if startlocation:
            print("开始图像找到，位置：", startlocation)
            # 如果识别到start图片，点击其中心位置
            start_center = pyscreeze.center(startlocation)
            pyautogui.click(start_center)
            K=K+1
            print("开始第"+str(K)+"局")
            time.sleep(15)
            run()
        else:
            print("开始图像未找到")
    except pyautogui.ImageNotFoundException:
        print("开始图像未找到，继续运行程序")
        # 在这里可以添加找不到图片时的处理逻辑
    except Exception as e:
        print("其他错误：", e)
        


    

    

print("脚本执行完毕")