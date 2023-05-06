"""
浏览器驱动放在与执行器的文件同目录 :  E:\liangqingyun\env\pyEnv\python.exe
使用文档地址(非官方) :https://python-selenium-zh.readthedocs.io/zh_CN/latest/1.%E5%AE%89%E8%A3%85/
官方文档 : https://www.selenium.dev/zh-cn/documentation/  不好看

新版本的selenium有变动 :
    参考官网 : https://www.selenium.dev/zh-cn/documentation/webdriver/getting_started/upgrade_to_selenium_4/

    # inputTag = driver.find_element_by_id("value")  # 利用ID查找
    # 改为：
    inputTag = driver.find_element(By.ID, "value")
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# 创建Chrome浏览器实例
driver = webdriver.Chrome()

# 打开一个网页
driver.get("https://www.google.com/")

# 模拟搜索
search_box = driver.find_element(by="name", value="q")
search_box.send_keys("Selenium Python")
search_box.send_keys(Keys.ENTER)

# 获取搜索结果
search_results = driver.find_elements(by=By.CSS_SELECTOR, value="div.g")
for result in search_results:
    title = result.find_element(by=By.TAG_NAME, value="h3")
    link = result.find_element(by=By.TAG_NAME, value="a")
    print(f"{title.text}: {link.get_attribute('href')}")

# 关闭浏览器
driver.quit()

