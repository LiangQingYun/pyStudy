import os
import speech_recognition as sr

from moviepy.video.io.VideoFileClip import VideoFileClip


def convert_video_to_audio(video_file, audio_file):
    # 创建视频文件剪辑
    video = VideoFileClip(video_file)
    # 获取视频的音频部分
    audio = video.audio
    # 保存音频文件
    audio.write_audiofile(audio_file)


def speech_to_text(audio_file_path):
    """
    将音频文件识别成文字
    :param audio_file_path: str，音频文件路径
    :return: str，识别结果
    """
    # 初始化语音识别器
    r = sr.Recognizer()

    # 读取音频文件
    try:
        with sr.AudioFile(audio_file_path) as source:
            audio = r.record(source)
        return r.recognize_google(audio, language='zh-CN')
    except sr.UnknownValueError:
        pass
    return None


def get_mp4_files(path):
    """
        拿到路径下的所有mp4文件
    """
    mp4_files = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".mp4"):
                mp4_files.append(os.path.join(root, file))
    return mp4_files


if __name__ == '__main__':
    path = r"\\10.10.10.116\video\第一批-159"
    mp4_files = get_mp4_files(path)

    results = []
    i = 0
    for mp4_file in mp4_files:
        filename = os.path.basename(mp4_file).split(".")[0]
        convert_video_to_audio(mp4_file, "E:\\shipin\\" + filename + ".wav")
        text = speech_to_text("E:\\shipin\\" + filename + ".wav")
        results.append(filename + ".mp4----------" + text)
        i += 1
        if i == 2:
            break

    print("\n")
    for result in results:
        print(result)

