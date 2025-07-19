import pyautogui
import pyscreeze
import time

# 设置颜色容差
tolerance = 200  # 可根据需要调整
target_color = (0, 255, 101)  # 示例：绿色

# 获取屏幕分辨率
screen_width, screen_height = pyautogui.size()
print(f"屏幕分辨率: {screen_width}x{screen_height}")

# 测试像素颜色
def test_pixel_color():
    while True:
        try:
            # 获取鼠标当前位置
            x, y = pyautogui.position()
            print(f"当前鼠标位置: ({x}, {y})")

            # 获取指定坐标的像素颜
            pixel_color = pyscreeze.pixel(x, y)
            print(f"像素颜色: {pixel_color}")

            # 检查颜色是否匹配
            if pyscreeze.pixelMatchesColor(x, y, target_color, tolerance):
                print(f"颜色匹配: {target_color}")
            else:
                print(f"颜色不匹配")

            # 等待一段时间后再次检测
            time.sleep(1)

        except KeyboardInterrupt:
            print("测试结束")
            break

# 运行测试
test_pixel_color()