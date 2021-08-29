from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

options = Options()
options.headless = True

path = "/Users/markono/Desktop/chromedriver"
browser = webdriver.Chrome(options=options, executable_path = path)
browser.get('https://en.wikipedia.org/wiki/List_of_largest_banks_in_the_United_States')
content = browser.find_elements_by_tag_name('tbody')
US_banks_table = content[0]

banks = US_banks_table.find_elements_by_xpath('./tr/td[2]/a')
print(len(banks))



browser.close()


