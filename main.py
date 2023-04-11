# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    import csv
    # q: newline是什么意思?
    with open('/data.csv', 'w', newline='') as csvFile:
        writer = csv.writer(csvFile)

        writer.writerow(['id', 'name', 'age'])
        writer.writerow(['10001', 'Mike', 20])
        writer.writerow(['10002', 'Bob', 22])
        writer.writerow(['10003', 'Jordan', 21])
    csvFile.close()






