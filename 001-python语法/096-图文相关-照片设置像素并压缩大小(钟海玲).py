from PIL import Image
import os

def compress_images(input_path, output_path):
    # 遍历指定文件夹中的所有文件和子文件夹
    for root, dirs, files in os.walk(input_path):
        for filename in files:
            # 检查文件是否为图像文件
            if filename.lower().endswith((".jpg", ".jpeg", ".png", ".bmp")):
                # 拼接文件路径
                filepath = os.path.join(root, filename)

                # 打开图像文件
                img = Image.open(filepath)

                # 如果图像模式为RGBA，转换为RGB模式
                if img.mode == "RGBA":
                    img = img.convert("RGB")

                # 调整图像大小
                img = img.resize((480, 640))

                # 初始化压缩质量和文件大小
                quality = 60
                size_kb = 0

                # 压缩图像并调整压缩质量，直到文件大小在30-40K之间
                while size_kb < 30 or size_kb > 40:
                    # 保存调整大小的图像并设置压缩质量
                    new_filename = filename.split(".")[0] + ".jpg"
                    save_path = os.path.join(output_path, os.path.relpath(root, input_path), new_filename)
                    os.makedirs(os.path.dirname(save_path), exist_ok=True)
                    img.save(save_path, optimize=True, quality=quality)

                    # 获取文件大小（以字节为单位）
                    size = os.path.getsize(save_path)

                    # 将字节转换为KB
                    size_kb = size/1024

                    # 如果文件大小小于30K，增加压缩质量
                    if size_kb < 30:
                        quality += 2
                    # 如果文件大小大于40K，减少压缩质量
                    elif size_kb > 40:
                        quality -= 2

                print(f"{filename}已成功缩小并压缩。")

# 测试代码
input_path = "E:/liangqingyun/新建文件夹/海珠谨培+资料"
output_path = "E:/liangqingyun/新建文件夹/newimage"
compress_images(input_path, output_path)
