from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

options = Options()
options.headless = True

path = "/Users/markono/Desktop/chromedriver"
browser = webdriver.Chrome(options=options, executable_path = path)
browser.get('https://bankchart.us/catalogue/banks')
content = browser.find_elements_by_class_name('abc-list_with-icon')


links = []
valid_websites = []

for div in content:
    link = div.find_element_by_tag_name('a')
    href = link.get_attribute('href')
    links.append(href)

for l in links:
    browser.get(l)
    bank_info = browser.find_elements_by_class_name('bank__info-item')

for info in bank_info:
    h5 = info.find_element_by_tag_name('h5')
    if (h5.text == "Web-site:"):
        website_link = info.find_element_by_tag_name('p').text
        valid_websites.append(website_link)
        print(website_link)

browser.close()
print(valid_websites)

