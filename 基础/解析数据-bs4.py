import os

filesnames = []
for root, dirs, files in os.walk(r"\\10.10.10.116\video\问答"):
    for file in files:
        file_path = os.path.join(root, file)
        if os.path.isfile(file_path) and file.upper().__contains__(r'MP4') :
            filesnames.append(file_path)
            print(file_path)

# print(filesnames)

