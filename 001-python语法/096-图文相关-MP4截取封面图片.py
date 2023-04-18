import subprocess
import os
import cv2

def extract_video_cover(input_path, output_path):
    """
    Extracts the cover image from the video file at input_path and saves it to output_path.
    """
    # Use FFmpeg to extract the cover image.
    subprocess.call(['ffmpeg', '-i', input_path, '-vframes', '1', '-q:v', '2', output_path])

def extract_all_video_covers(input_dir, output_dir):
    # 遍历指定目录下的所有文件和目录，包括子目录
    for root, dirs, files in os.walk(input_dir):
        for filename in files:
            # 如果是 mp4 文件
            if filename.endswith('.mp4'):
                # 构造输入和输出路径
                input_path = os.path.join(root, filename)
                output_path = os.path.join(output_dir, os.path.splitext(filename)[0] + '.jpg')
                # 提取视频封面并保存
                extract_video_cover(input_path, output_path)

# 指定输入和输出路径
input_dir = r'\\10.10.10.116\video\第一批-159'
output_dir = r'E:\shipin\image'

# 提取所有视频封面
extract_all_video_covers(input_dir, output_dir)
