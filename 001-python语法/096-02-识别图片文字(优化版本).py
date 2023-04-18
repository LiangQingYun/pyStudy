import os

import cv2
import numpy as np
import pytesseract
from PIL import Image

def recognize_text(image_path):
    # 读取图片
    img = Image.open(image_path)
    # 转换为OpenCV可处理的格式
    img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

    # 灰度化处理
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 二值化处理
    _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # 去噪处理
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    thresh = cv2.erode(thresh, kernel, iterations=1)
    thresh = cv2.dilate(thresh, kernel, iterations=1)

    # 识别图片文字内容
    text = pytesseract.image_to_string(thresh, lang='chi_sim')

    return text.replace(" ", "")


def recognize_all_images(folder_path):
    # 获取文件夹下所有文件和子文件夹下的所有文件
    file_list = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith('.jpg') or file.lower().endswith('.png'):
                file_list.append(os.path.join(root, file))

    # 识别所有图片中的文字
    for file_path in file_list:
        text = recognize_text(file_path)
        print(f"{file_path} 中的文字为：{text}")


# 示例：识别 E:\shipin\image 文件夹下所有图片中的文字
recognize_all_images("E:\\shipin\\image")
