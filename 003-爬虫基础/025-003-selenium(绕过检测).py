
from selenium import webdriver
browser = webdriver.Chrome()

# 无处理
browser.get('https://bot.sannysoft.com/')

# 设置屏蔽
options = webdriver.ChromeOptions()
print(options.default_capabilities)
options.add_argument('--disable-blink-features=AutomationControlled')
browsers = webdriver.Chrome(chrome_options=options)
browsers.get('https://bot.sannysoft.com/')
