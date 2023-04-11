# import os
#
#
# # 获取指定路径下的所有文件和路径
# def get_files(path):
#     # 判断路径是否存在
#     if not os.path.exists(path):
#         print("指定路径不存在！")
#         return
#
#     # 获取指定路径下的所有文件和路径
#     files = []
#     for dirpath, dirnames, filenames in os.walk(path):
#         for dirname in dirnames:
#             files.append(os.path.join(dirpath, dirname))
#         for filename in filenames:
#             files.append(os.path.join(dirpath, filename))
#
#     return files
#
#
# # 测试
#
# filesnames = []
# for root, dirs, files in os.walk(r"\\10.10.10.116\video\问答"):
#     for file in files:
#
#         file_path = os.path.join(root, file)
#         if os.path.isfile(file_path) and file.upper().__contains__(r'MP4') :
#             filesnames.append(file_path)
#
# # print(filesnames)
# #
# import difflib
# #
# # str1 = '湿疹护理的误区（1）'
# # str2 = '15.湿疹护理的误区.1.mp4'
# #
# # str1 = '湿疹护理的误区（2）'
# # str2 = '16.湿疹护理的误区.2.mp4'
# #
# # similarity = difflib.SequenceMatcher(None, str1, str2).ratio()
# # print(similarity) # 0.7
#
# import xlrd
#
# file_path = r'E:\1111.xls'
# workbook = xlrd.open_workbook(file_path)
# sheet = workbook.sheet_by_index(0)
#
# # 获取第一列的所有值
# column_values = sheet.col_values(0)
#
# # 输出第一列的所有值
# similarity_tmp = -1
# fname = ''
# for value in column_values:
#     for filesname in filesnames:
#         fn = filesname.split('\\')[-1]
#         result = fn[fn.rfind('/') + 1:]
#         similarity = difflib.SequenceMatcher(None, value, result).ratio()
#         if similarity > similarity_tmp and similarity > 0.5:
#             similaritytmp = similarity
#             fname = filesname
#
#     if fname.__contains__('成品'):
#         print(value, '-------', fname)
#     else:
#         print(value, '-------')
#     similarity_tmp = -1
#     fname = ''
#
#
from pyasn1.compat.octets import null


def flatten_json(json_data, parent_key='', result=None):
    if result is None:
        result = []
    if isinstance(json_data, dict):
        for key, value in json_data.items():
            if isinstance(value, list):
                for i, v in enumerate(value):
                    new_key = parent_key + '-' + key
                    flatten_json(v, new_key, result)
            else:
                new_key = parent_key + '-' + key if parent_key else key
                flatten_json(value, new_key, result)
    else:
        result.append(f'{parent_key}-{json_data}')
    return result


json_data = {
    "code": 1,
    "msg": "操作成功",
    "data": {
        "DrugChatTips": [
            {
                "Type": null,
                "Platform": null,
                "Content": 1,
                "Id": null,
                "Result": "非暂时开放",
                "Genericname": "卡培他滨片"
            },
            {
                "Type": null,
                "Platform": null,
                "Content": null,
                "Id": null,
                "Result": "非暂时开放",
                "Genericname": "卡培他滨片"
            }
        ]
    }
}

result = flatten_json(json_data)
print(result)
