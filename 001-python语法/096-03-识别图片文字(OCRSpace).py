import os
import requests
import json

def recognize_text(image_file_path, api_key):
    """
    使用 OCR.space API 识别图片中的文字

    Args:
        image_file_path (str): 待识别的图片文件路径
        api_key (str): OCR.space API 的密钥     key:  K82717532288957

    Returns:
        str: 识别结果
    """
    # OCR.space API 的网址
    api_url = 'https://api.ocr.space/parse/image'

    # 构造 API 请求参数
    payload = {
        'apikey': api_key,
        'language': 'chs',
        'isOverlayRequired': False
    }

    # 发送 API 请求
    with open(image_file_path, 'rb') as f:
        r = requests.post(api_url, files={'image': f}, data=payload)

    # 解析 API 返回结果
    result = json.loads(r.content.decode())

    # 提取识别结果
    if result['IsErroredOnProcessing'] or result['ParsedResults'][0]['ErrorMessage']:
        print('Error:', result['ErrorMessage'])
        return ''
    else:
        text = result['ParsedResults'][0]['ParsedText']
        return text




def recognize_all_images(folder_path):
    # 获取文件夹下所有文件和子文件夹下的所有文件
    file_list = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith('.jpg') or file.lower().endswith('.png'):
                file_list.append(os.path.join(root, file))

    # 识别所有图片中的文字
    for file_path in file_list:
        text = recognize_text(file_path, 'K82717532288957')
        print(f"{file_path} ------- {text}")


# 示例：识别 E:\shipin\image 文件夹下所有图片中的文字
recognize_all_images("E:\\shipin\\image")
