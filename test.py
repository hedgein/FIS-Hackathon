from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

options = Options()
options.headless = True

path = "/Users/markono/Desktop/chromedriver"
browser = webdriver.Chrome(options=options, executable_path = path)
browser.get('https://bankchart.us/catalogue/banks')
content = browser.find_elements_by_class_name('abc-list_with-icon')
print(len(content))
browser.close()