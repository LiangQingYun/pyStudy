import pandas as pd

# 读取两个excel表格，保存为 DataFrame 对象
df1 = pd.read_excel('D:\\姓名专业.xlsx')
df2 = pd.read_excel('D:\\专业科目.xlsx')

# 通过列 A 进行关联，生成新的 DataFrame 对象
merged = pd.merge(df1, df2, on='专业', how='outer')

# 输出结果到 excel 文件的 sheet3 中
with pd.ExcelWriter('D:\\姓名专业科目.xlsx') as writer:
    merged.to_excel(writer, sheet_name='sheet1', index=False)
