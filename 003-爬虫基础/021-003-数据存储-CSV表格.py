import csv


class ali:
    def __init__(self):
        # 初始化爬虫
        pass

    def get_data(self):
        # 获取数据
        pass

    def parse_data(self):
        # 解析数据
        pass

    def save_data(self):
        # 保存数据
        pass


# 读取CSV文件，使用分号作为分隔符
with open('data.csv', 'r', newline='') as f:
    reader = csv.reader(f, delimiter=';')
    for row in reader:
        print(row)

# 写入CSV文件，使用Tab作为分隔符
with open('data.csv', 'w', newline='') as f:
    writer = csv.writer(f, delimiter='\t')
    writer.writerow(['Name', 'Age', 'Gender'])
    writer.writerow(['Alice', '25', 'Female'])
    writer.writerow(['Bob', '30', 'Male'])
