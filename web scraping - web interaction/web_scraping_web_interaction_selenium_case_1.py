# 1. Import Selenium module
#   a) import Options - optional if you want to open Chrome session in specific profile (google for more)
#   b) import time - optional in case when time.sleep(secs) is necessary - in this case - waiting for website to load
#      before clicking
# 2. Pass chrome driver path as Service object
# 3. Initialize webdriver object
# 4. Getting element using [web driver object].get("URL")
# 5. Find element/elements and retrieving data:
#    -- As 1st argument ATTRIBUTE_TYPE/TAG_TYPE should be provided and as 2nd ATTRIBUTE_VALUE/TAG_VALUE --
# 	a) retrieving elements' value (as a string) using .text
# 	b) retrieving elements' attribute value using .get_attribue("[attribute_name]")
#   c) retrieving elements' value in case element does not have easy identifiable attribute/tag
#      using "css selector"
#   d) retrieving elements' value using XPath - especially useful in case if other methods failed
#   e) retrieving many elements values; accessing element and its subelements values
# 6. Autoclicking bot example
# 7. [webdriver object].close() or [webdriver object].quit()
#    -- close() closes opened tab and quit() shuts entire browser --


# *1.
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pprint
# *1.a)
from selenium.webdriver.chrome.options import Options
# *1.b)
import time

# *2.
s = Service('C:\Development\chromedriver\chromedriver.exe')
# *3.
driver = webdriver.Chrome(service=s)
# # *4.
# driver.get("https://www.amazon.com/Xbox-S/dp/B08G9J44ZN")
# *5.
price = driver.find_element("id", "priceblock_ourprice")
# *5.a)
print(price.text)
# *5.b)
print(price.get_attribute("id"))

# *5.c)
driver.get("https://www.python.org/")
doc_link = driver.find_element("css selector", ".documentation-widget a")
print(doc_link.text)

# *5.d)
driver.get("https://www.python.org/")
doc_link_xpath = driver.find_element("xpath", '//*[@id="content"]/div/section/div[1]/div[3]/p[2]/a')
print(doc_link_xpath.text)

# *5.e)
driver.get("https://www.python.org/")
upcoming_events = driver.find_elements("css selector", ".medium-widget.event-widget.last li")
upcoming_events_list = []
for _ in upcoming_events:
    temp_element = {
        'time': _.find_element('css selector', 'time').text,
        'event': _.find_element('css selector', 'a').text
    }
    upcoming_events_list.append(temp_element)
pprint.pprint(upcoming_events_list)

# *6. - items clicking
for i in range(4):
    driver.get("https://toshl.com/app/#/expense-categories")
    time.sleep(2)
    category_raw = driver.find_element("css selector", 'body > div.tc-mc_container.t-inline-dialog-container > div > div.tc-sl_main > t-scroller > div.t-scroller_scroll > div.t-scroller_content > div.tc-sl_main_include > div > div > t-tags-sorting > div > div.td-tags-sorting_categories.pad-top-48.gs_relative > div.tt-content > t-manage-boxes > div:nth-child(1) > div > div.td-mb_box_title_group')
    category_raw.click()
    time.sleep(2)
    del_1 = driver.find_element("css selector", '.tc-dialog_right')
    del_1.click()
    time.sleep(2)
    del_2 = driver.find_element("css selector", '.t2-btn')
    del_2.click()
    time.sleep(2)
    del_3 = driver.find_element("css selector", '.t2-btn.red')
    del_3.click()

for i in range(22):
    driver.get("https://toshl.com/app/#/expense-categories")
    time.sleep(2)
    driver.find_element("css selector", ".t2-hover")
    time.sleep(2)
    driver.find_element("link text", "Edit tag")
    time.sleep(2)
    driver.find_element("css selector", ".t2-btn")
    time.sleep(2)
    driver.find_element("css selector", ".t2-btn.red")





driver.get("https://orteil.dashnet.org/cookieclicker/")
time.sleep(1.5)
language = driver.find_element(by="css selector", value=".langSelectButton")
language.click()
time.sleep(1.5)
cookie_button = driver.find_element(by="css selector", value="#bigCookie")
for i in range(5000):
    for i in range(500):
        cookie_button.click()
    time.sleep(7)

# *7.
driver.close()
#
# driver.quit()
# '''Quits entire browser'''
#
# driver.close()
# '''Demonstrates triple double quotes
# docstrings and does nothing really.'''