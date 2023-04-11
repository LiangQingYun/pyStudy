import json


def json_contains(out_json, in_json):
    """
    判断outjson是否包含injson
    """
    # 将JSON解析为字典
    dict1 = json.loads(out_json)
    dict2 = json.loads(in_json)

    # 递归地检查是否包含
    return contains(dict1, dict2)


def contains(dict1, dict2):
    """
    递归地检查字典是否包含在另一部字典中
    """
    # 检查dict2中的所有键是否都在dict1中存在
    for key2 in dict2:
        if key2 not in dict1:
            return False

    # 检查dict2中的所有值是否都在dict1中存在，如果是字典或列表则递归调用contains函数
    for key2, value2 in dict2.items():
        value1 = dict1[key2]
        if isinstance(value2, dict):
            if not contains(value1, value2):
                return False
        elif isinstance(value2, list):
            if not contains_list(value1, value2):
                return False
        elif value1 != value2:
            return False

    return True


def contains_list(list1, list2):
    """
    递归地检查列表中的元素是否都在另一个列表中存在
    """
    for item2 in list2:
        found = False
        for item1 in list1:
            if isinstance(item2, dict):
                if contains(item1, item2):
                    found = True
                    break
            elif isinstance(item2, list):
                if contains_list(item1, item2):
                    found = True
                    break
            elif item1 == item2:
                found = True
                break
        if not found:
            return False
    return True


if __name__ == '__main__':
    out_json = {
        "code": 1,
        "msg": "操作成功",
        "data": {
            "DrugChatTips": [
                {
                    "Type": None,
                    "Platform": None,
                    "Content": 1,
                    "Id": None,
                    "Result": "非暂时开放",
                    "Genericname": "卡培他滨片"
                },
                {
                    "Type": None,
                    "Platform": None,
                    "Content": None,
                    "Id": None,
                    "Result": "非暂时开放",
                    "Genericname": "卡培他滨片"
                }
            ]
        }
    }

    in_json = {
        "code": 1,
        "msg": "操作成功",
        "data": {
            "DrugChatTips": [
                {
                    "Type": None,
                    "Platform": None,
                    "Content": 1,
                    "Id": None,
                    "Result": "非暂时开放",
                    "Genericname": "卡培他滨片"
                },
                {
                    "Type": None,
                    "Platform": None,
                    "Content": None,
                    "Id": None,
                    "Result": "非暂时开放",
                    "Genericname": "卡培他滨片"
                }
            ]
        }
    }

    print(json_contains(json.dumps(out_json), json.dumps(in_json)))
