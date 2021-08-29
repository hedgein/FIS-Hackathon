import selenium
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

bank_names = []
bank_links = []

for b in banks:
    clas = b.get_attribute('class')
    if (clas == "new"):
            continue

    title = b.get_attribute('title')
    bank_names.append(title)
    link = b.get_attribute('href')
    bank_links.append(link)

print(bank_names)
print(bank_links)
for l in bank_links:
    browser.get(l)
    try:
        official_website = browser.find_element_by_partial_link_text('website').text
        bank_links.append(official_website)
    except selenium.common.exceptions.NoSuchElementException:
        continue

print(bank_links)

browser.close()


