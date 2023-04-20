from aip import AipOcr
import os

APP_ID = '32536167'
API_KEY = 'g8W4IxDMG1qfP3M4lBjaMnRc'
SECRET_KEY = 'jUxCN2BF9rWt96359QNaVMB74jC5srEE'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)


def get_text_from_image(image_path):
    with open(image_path, 'rb') as f:
        image = f.read()
    result = client.basicGeneral(image)
    if 'words_result' in result:
        return result['words_result']
    return None


image_dir = 'E:/shipin/image'
for filename in os.listdir(image_dir):
    if filename.endswith('.jpg') or filename.endswith('.png'):
        image_path = os.path.join(image_dir, filename)
        text_list = get_text_from_image(image_path)
        if text_list:
            text_str = '\n'.join([text['words'] for text in text_list]).replace('\n', '')
            print(f'{filename} ------ {text_str}')
        else:
            print(f'{filename} ------ 无法识别')


