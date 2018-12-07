from selenium.webdriver import Chrome,ActionChains
import time

browser = Chrome()
url = "https://weibo.com/"

browser.get(url)
time.sleep(5)
browser.find_element_by_link_text('登录').click()
title = browser.title
print(title)
time.sleep(0.5)
browser.find_element_by_link_text('安全登录').click()
while browser.title == title:
    time.sleep(0.5)
print(browser.title)
follow_url = browser.find_elements_by_xpath('//li[@class="S_line1"]/a[@bpfilter="page_frame"]')[0].get_attribute("href")
browser.get(follow_url)
print(browser.title)
follows = browser.find_elements_by_xpath('//p[@class="pic_box"]/a/img')
follows_name = [x.get_attribute("title") for x in follows]
for i in range(len(follows_name)):
    browser.find_element_by_link_text(follows_name[i]).click()
    browser.switch_to.window(browser.window_handles[1])
    time.sleep(3)
    fans_url = browser.find_elements_by_xpath('//h2/a[@class="S_txt1"]')[1].get_attribute("href")
    browser.get(fans_url)
    print(browser.title)
    fans = browser.find_elements_by_xpath('//dt[@class="mod_pic"]/a/img')
    fans_name = [x.get_attribute("alt") for x in fans]

    next_page = browser.find_elements_by_xpath('//a[@bpfilter="page"]')[6].get_attribute("href")
    while next_page:
        browser.get(next_page)
        fans = browser.find_elements_by_xpath('//dt[@class="mod_pic"]/a/img')
        fans_name.append(x.get_attribute("alt") for x in fans)
        next_page = browser.find_elements_by_xpath('//a[@bpfilter="page"]')[6].get_attribute("href")
    break
    # browser.switch_to.window(follow_handle)

# driver = Chrome()
# url = "https://weibo.com/209931333"
# driver.get(url)
# print(driver.current_url)
# while driver.current_url != url:
#     time.sleep(0.5)
# # response = driver.page_source.encode('utf-8')
# # with open('response.html', 'wb') as f:
# #     f.write(response)
# f = driver.find_elements_by_xpath('//h2/a[@class="S_txt1"]')