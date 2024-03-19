'''
computer_vision experiment
reference: https://blog.csdn.net/Python_0011/article/details/131871546
author: alalpaca
date: 2024/3/13 8:27
'''

import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

"""
test:

cap = cv2.VideoCapture(0)        #'0'选择笔记本电脑自带参数，‘1’为USB外置摄像头
print(cap.get(3), cap.get(4))    #验证是否设置成功
while (True):
    ret, frame = cap.read()      #读取图像并显示
    frame = cv2.flip(frame, 1)
    # show a frame
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'): #按‘q’键退出后，释放摄像头资源
        cv2.imwrite("test.png", frame)  # 拍摄图像的保存路径
        break
cap.release()
cv2.destroyAllWindows()

"""

# task1:
# 1. read an image
# 2. print name on it
# 3. save to local

def show_chinese(img, text, pos):
    """
    :param img: opencv 图片
    :param text: 显示的中文字体
    :param pos: 显示位置
    :return:    带有字体的显示图片（包含中文）
    """
    img_pil = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))  # 这一行将OpenCV图像从BGR颜色空间转换为RGB颜色空间，并使用PIL库创建一个PIL图像对象
    font = ImageFont.truetype(font='msyh.ttc', size=20)              # 该字体文件通常包含中文字符
    draw = ImageDraw.Draw(img_pil)                                   # 创建一个PIL图像的绘图对象draw，以便在图像上绘制文本。
    draw.text(pos, text, font=font, fill=(255, 255, 255))  # PIL中RGB=(255,0,0)表示红色
    img_cv = np.array(img_pil)                         # PIL图片转换为numpy，以便进一步用opencv处理
    img = cv2.cvtColor(img_cv, cv2.COLOR_RGB2BGR)      # PIL格式转换为OpenCV的BGR格式
    return img

image= cv2.imread("cat.jpeg", cv2.IMREAD_COLOR)
# 显示全黑图像原因：不支持jpg,需jpeg
cv2.imshow('image', image)
# cv2.resizeWindow("image", 500, 400)
cv2.waitKey(0)
cv2.destroyAllWindows()

# image_putText = image.copy()
# text = '21122884 汪蕴斐'
# cv2.putText(image_putText, text, (50, 200),cv2.QT_FONT_BLACK, 0.85, (255, 255, 255))
# cv2.imshow('text_image', image_putText)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

img = image.copy()
text = '21122884 汪蕴斐'
img = show_chinese(img, text, (50, 200))
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('cat_text.jpeg', img)


# task2:
# read a local video and play

import cv2

def play_video(video_path):
    cap = cv2.VideoCapture(video_path)
    # 检查视频是否成功打开
    if not cap.isOpened():
        print("Error: 无法打开视频文件。")
        return
    # 循环读取帧并播放视频
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: 无法读取视频帧。")
            break
        cv2.imshow('Video', frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):  # 按下 'q' 键退出循环
            break
    cap.release()
    cv2.destroyAllWindows()

video_path = 'Waymo.mp4'
play_video(video_path)
