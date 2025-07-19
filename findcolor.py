import cv2
import numpy as np
from collections import defaultdict

def get_dominant_color(image_path):
    # 读取图像
    image = cv2.imread(image_path)
    
    # 将图像从BGR颜色空间转换为HSV颜色空间
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    # 定义颜色范围（以紫色为例）
    lower_purple = np.array([135, 50, 50])  # 紫色的低阈值
    upper_purple = np.array([150, 255, 255])  # 紫色的高阈值
    
    # 创建掩码，找出紫色区域
    purple_mask = cv2.inRange(hsv_image, lower_purple, upper_purple)
    
    # 统计紫色像素的数量
    purple_pixel_count = np.sum(purple_mask) // 255  # 每个像素值为255，所以除以255得到像素数量
    
    # 如果紫色像素数量占总像素的一定比例，认为紫色是主要颜色
    total_pixels = image.shape[0] * image.shape[1]
    if purple_pixel_count / total_pixels > 0.1:  # 假设紫色像素占比超过10%
        return (128, 0, 128)  # 紫色的RGB值
    
    # 如果不是紫色，可以继续处理其他颜色
    # 这里简化处理，直接返回黑色作为示例
    return (0, 0, 0)

# 示例用法
image_path = 'du.png'  # 替换为你的图片路径
dominant_color = get_dominant_color(image_path)
print(f"图片的主要颜色值（RGB）：{dominant_color}")