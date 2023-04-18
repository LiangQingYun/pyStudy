from PIL import Image
import pytesseract

# 读取图片
image = Image.open("../10010-image/中文-简单.jpg")

# 识别图片中的中文文字
text = pytesseract.image_to_string(image, lang='chi_sim')

# 打印识别结果
print(text)


