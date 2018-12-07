from selenium.webdriver import Chrome, ActionChains
import time, requests, re, os

browser = Chrome(r"E:\JetBrains\browser\chromedriver.exe")
url = "https://qzone.qq.com/"
path = r"C:\Users\Administrator.YLMF-20150729SV\Desktop\qzone"
browser.get(url)
# browser.fullscreen_window()
while browser.current_url == url:
    time.sleep(0.5)
time.sleep(5)
browser.find_element_by_xpath("//li[@class='menu_item_4']/a[@tabindex]").click()
print(browser.title)
time.sleep(5)

for i in range(50):
    browser.switch_to.default_content()
    elem = browser.find_element_by_class_name('app_canvas_frame')
    browser.switch_to.frame(elem)
    time.sleep(1)
    list = browser.find_elements_by_xpath('//ul[@class="js-album-list-ul"]//a[@class="c-tx2 js-album-desc-a"]')[i]
    if not os.path.exists(path + '\\' + list.text):
        os.mkdir(path + '\\' + list.text)
    print(i, '\t', list.text)
    list.click()
    time.sleep(5)
    browser.switch_to.default_content()
    elem = browser.find_element_by_class_name('app_canvas_frame')
    browser.switch_to.frame(elem)
    # time.sleep(1)
    images_url = browser.find_elements_by_xpath('//a/img[@class="j-pl-photoitem-img"]')
    j = 0
    for image in images_url:
        print(j, image.get_attribute("src"))
        j += 1
    # break
    browser.back()
    time.sleep(5)
    # print(browser.title)

# for content in list:
#     # print(content.text)
#     print('sucess')
#     browser.find_element_by_link_text(content.text).click()
#     browser.back()
# elem = browser.find_element_by_class_name('app_canvas_frame')
# browser.switch_to.frame(elem)

# browser.switch_to.default_content()
# browser.switch_to.frame('userData_iframe__Y_popTips')
# list2 = browser.find_elements_by_xpath('//ul[@class="js-album-list-ul"]/li')
# print(list2)
# for l in list:
#     print(l.text)
# ActionChains(browser).move_by_offset(30,600).click()
# ActionChains(browser).move_by_offset(10,10)
# time.sleep(20)
# browser.quit()

# response = browser.page_source.encode('utf-8')
# with open('response.html', 'wb') as f:
#     f.write(response)
# browser.find_element_by_xpath('//ul[@class="js-album-list-ul"]//a').click()


# driver = webdriver.PhantomJS(executable_path=r'E:\phantomjs-2.1.1-windows\bin\phantomjs.exe')
# response = driver.page_source.encode('utf-8')
# driver.get('https://ssl.ptlogin2.qq.com/ptqrshow?appid=549000912'
#            '&e=2&l=M&s=3&d=72&v=4&t=0.6947577807468706&daid=5&pt_3rd_aid=0')


# driver.save_screenshot("001.png")
# Image.open('001.png').show()
# time.sleep(5)
# driver.get('https://qzone.qq.com/')
# with open('response.html', 'wb') as f:
#     f.write(response)
# driver.save_screenshot("002.png")
# Image.open('002.png').show()
# # pattern = re.compile('https://ssl.ptlogin2.qq.com/ptqrshow.*aid=0')
# # images_url = re.findall(pattern, response)
# # print(images_url)
# driver.quit()


# driver.find_element_by_xpath("//li[@class='reg-tab-nav']").click()
# driver.find_element_by_name("mobile").send_keys(str(input("请输入手机号：")))
# driver.find_element_by_id("pw").send_keys("abc123")
# driver.find_element_by_xpath("//div[@class='fbox-main clearfix zg-code-box']/button").click()
# code_url = 'https://passport.17173.com/register/captcha'
# code_data = requests.Session().get(code_url,headers = {"User-Agent" : "Mozilla/5.0"}).content
# with open("26ph_code.jpg", "wb") as f:
#     f.write(code_data)
# time.sleep(1)
# code = input("请输入验证码：")
# driver.find_element_by_class_name("form-text").send_keys(code)
# driver.find_element_by_xpath("//button[@id='submit_validate_code']").click()
# time.sleep(1)
# driver.save_screenshot("26_phone2.png")



# http://b269.photo.store.qq.com/psb?/V13Api2e4EkLWV/iUZ7AyvPKle1FEfDtPW2ALtzbSs6eYuKrLDX13*KkoQ!/m/dA0BAAAAAAAAnull&bo=AAW.BjAMcBARCd8!&rf=photolist&t=5
# http://b269.photo.store.qq.com/psb?/V13Api2e4EkLWV/iUZ7AyvPKle1FEfDtPW2ALtzbSs6eYuKrLDX13*KkoQ!/b/dA0BAAAAAAAA&bo=AAW.BjAMcBARCd8!&rf=viewer_4
#
# http://b105.photo.store.qq.com/psb?/V13Api2e4EkLWV/0cS3ScF9b3yrX4DG6Julnw5rzTVyGTp3jAmbuUvXR6M!/m/dGkAAAAAAAAAnull&bo=AAW1AwAFtQMRCT4!&rf=photolist&t=5
# http://b105.photo.store.qq.com/psb?/V13Api2e4EkLWV/0cS3ScF9b3yrX4DG6Julnw5rzTVyGTp3jAmbuUvXR6M!/b/dGkAAAAAAAAA&bo=AAW1AwAFtQMRCT4!&rf=viewer_4
#
# /m/ = /b/
# null&bo = &bo
# photolist&t=5 = viewer_4
#
# http://b366.photo.store.qq.com/psb?/9310b0a1-8c39-4850-98bd-8cb6e4dfc806/ro7s*UoM4DbOz4YKc6JiY7nySQ.DeowkXwkYetNmp9Q!/m/dG4BAAAAAAAAnull&bo=wAMABcADAAURCT4!&rf=photolist&t=5
# http://b366.photo.store.qq.com/psb?/9310b0a1-8c39-4850-98bd-8cb6e4dfc806/ro7s*UoM4DbOz4YKc6JiY7nySQ.DeowkXwkYetNmp9Q!/b/dG4BAAAAAAAA&bo=wAMABcADAAURCT4!&rf=viewer_4
#
# http://b269.photo.store.qq.com/psb?/V13Api2e4EkLWV/iUZ7AyvPKle1FEfDtPW2ALtzbSs6eYuKrLDX13*KkoQ!/m/dA0BAAAAAAAAnull&bo=AAW.BjAMcBARCd8!&rf=photolist&t=5
# http://b269.photo.store.qq.com/psb?/V13Api2e4EkLWV/iUZ7AyvPKle1FEfDtPW2ALtzbSs6eYuKrLDX13*KkoQ!/b/dA0BAAAAAAAA&bo=AAW.BjAMcBARCd8!&rf=viewer_4
# http://r.photo.store.qq.com/psb?/V13Api2e4EkLWV/iUZ7AyvPKle1FEfDtPW2ALtzbSs6eYuKrLDX13*KkoQ!/r/dA0BAAAAAAAA
#
# b[1~9] = r
# /m/ = r
#
# app_canvas_frame xh-highlight

# from selenium.webdriver import Chrome, ActionChains
# import time, requests, re, os
#
# browser = Chrome(r"E:\JetBrains\browser\chromedriver.exe")
# url = "https://qzone.qq.com/"
# path = r"C:\Users\Administrator.YLMF-20150729SV\Desktop\qzone"
# browser.get(url)
# # browser.fullscreen_window()
# browser.switch_to.frame('login_frame')
# browser.find_element_by_xpath('//*[@id="qlogin_list"]/a[1]').click()
# while browser.current_url == url:
#     time.sleep(0.5)
# time.sleep(5)
# browser.find_element_by_xpath("//li[@class='menu_item_4']/a[@tabindex]").click()
# print(browser.title)
# time.sleep(5)
# elem = browser.find_element_by_class_name('app_canvas_frame')
# inner = elem.get_attribute('content')
# print(inner)
# # elem.__setattr__('scrolling', 'yes')
# # elem.__setattr__('allowtransparency', 'no')
# # elem.__setattr__('frameborder', 'yes')
# # browser.switch_to.frame(elem)
# #
# # list = browser.find_elements_by_xpath('//*[@id="js-album-list-noraml"]/div/div/ul/li/div')
# # print(len(list))
# # response = browser.page_source.encode('utf-8')
# # with open('response.html', 'wb') as f:
# #     f.write(response)
#
# # for i in range(50):
# #     browser.switch_to.default_content()
# #     elem = browser.find_element_by_class_name('app_canvas_frame')
# #     browser.switch_to.frame(elem)
# #     time.sleep(1)
# #     list = browser.find_elements_by_xpath('//ul[@class="js-album-list-ul"]//a[@class="c-tx2 js-album-desc-a"]')[i]
# #     if not os.path.exists(path + '\\' + list.text):
# #         os.mkdir(path + '\\' + list.text)
# #     print(i, '\t', list.text)
# #     list.click()
# #     time.sleep(5)
# #     browser.switch_to.default_content()
# #     elem = browser.find_element_by_class_name('app_canvas_frame')
# #     browser.switch_to.frame(elem)
# #     # time.sleep(1)
# #     images_url = browser.find_elements_by_xpath('//a/img[@class="j-pl-photoitem-img"]')
# #     j = 0
# #     for image in images_url:
# #         print(j, image.get_attribute("src"))
# #         j += 1
# #     # break
# #     browser.back()
# #     time.sleep(5)
# #     # print(browser.title)
#
# # for content in list:
# #     # print(content.text)
# #     print('sucess')
# #     browser.find_element_by_link_text(content.text).click()
# #     browser.back()
# # elem = browser.find_element_by_class_name('app_canvas_frame')
# # browser.switch_to.frame(elem)
#
# # browser.switch_to.default_content()
# # browser.switch_to.frame('userData_iframe__Y_popTips')
# # list2 = browser.find_elements_by_xpath('//ul[@class="js-album-list-ul"]/li')
# # print(list2)
# # for l in list:
# #     print(l.text)
# # ActionChains(browser).move_by_offset(30,600).click()
# # ActionChains(browser).move_by_offset(10,10)
# # time.sleep(20)
# # browser.quit()
#
# # response = browser.page_source.encode('utf-8')
# # with open('response.html', 'wb') as f:
# #     f.write(response)
# # browser.find_element_by_xpath('//ul[@class="js-album-list-ul"]//a').click()
#
#
# # driver = webdriver.PhantomJS(executable_path=r'E:\phantomjs-2.1.1-windows\bin\phantomjs.exe')
# # response = driver.page_source.encode('utf-8')
# # driver.get('https://ssl.ptlogin2.qq.com/ptqrshow?appid=549000912'
# #            '&e=2&l=M&s=3&d=72&v=4&t=0.6947577807468706&daid=5&pt_3rd_aid=0')
#
#
# # driver.save_screenshot("001.png")
# # Image.open('001.png').show()
# # time.sleep(5)
# # driver.get('https://qzone.qq.com/')
# # with open('response.html', 'wb') as f:
# #     f.write(response)
# # driver.save_screenshot("002.png")
# # Image.open('002.png').show()
# # # pattern = re.compile('https://ssl.ptlogin2.qq.com/ptqrshow.*aid=0')
# # # images_url = re.findall(pattern, response)
# # # print(images_url)
# # driver.quit()
#
#
# # driver.find_element_by_xpath("//li[@class='reg-tab-nav']").click()
# # driver.find_element_by_name("mobile").send_keys(str(input("请输入手机号：")))
# # driver.find_element_by_id("pw").send_keys("abc123")
# # driver.find_element_by_xpath("//div[@class='fbox-main clearfix zg-code-box']/button").click()
# # code_url = 'https://passport.17173.com/register/captcha'
# # code_data = requests.Session().get(code_url,headers = {"User-Agent" : "Mozilla/5.0"}).content
# # with open("26ph_code.jpg", "wb") as f:
# #     f.write(code_data)
# # time.sleep(1)
# # code = input("请输入验证码：")
# # driver.find_element_by_class_name("form-text").send_keys(code)
# # driver.find_element_by_xpath("//button[@id='submit_validate_code']").click()
# # time.sleep(1)
# # driver.save_screenshot("26_phone2.png")
#
#
# # http://b269.photo.store.qq.com/psb?/V13Api2e4EkLWV/iUZ7AyvPKle1FEfDtPW2ALtzbSs6eYuKrLDX13*KkoQ!/m/dA0BAAAAAAAAnull&bo=AAW.BjAMcBARCd8!&rf=photolist&t=5
# # http://b269.photo.store.qq.com/psb?/V13Api2e4EkLWV/iUZ7AyvPKle1FEfDtPW2ALtzbSs6eYuKrLDX13*KkoQ!/b/dA0BAAAAAAAA&bo=AAW.BjAMcBARCd8!&rf=viewer_4
# #
# # http://b105.photo.store.qq.com/psb?/V13Api2e4EkLWV/0cS3ScF9b3yrX4DG6Julnw5rzTVyGTp3jAmbuUvXR6M!/m/dGkAAAAAAAAAnull&bo=AAW1AwAFtQMRCT4!&rf=photolist&t=5
# # http://b105.photo.store.qq.com/psb?/V13Api2e4EkLWV/0cS3ScF9b3yrX4DG6Julnw5rzTVyGTp3jAmbuUvXR6M!/b/dGkAAAAAAAAA&bo=AAW1AwAFtQMRCT4!&rf=viewer_4
# #
# # /m/ = /b/
# # null&bo = &bo
# # photolist&t=5 = viewer_4
# #
# # http://b366.photo.store.qq.com/psb?/9310b0a1-8c39-4850-98bd-8cb6e4dfc806/ro7s*UoM4DbOz4YKc6JiY7nySQ.DeowkXwkYetNmp9Q!/m/dG4BAAAAAAAAnull&bo=wAMABcADAAURCT4!&rf=photolist&t=5
# # http://b366.photo.store.qq.com/psb?/9310b0a1-8c39-4850-98bd-8cb6e4dfc806/ro7s*UoM4DbOz4YKc6JiY7nySQ.DeowkXwkYetNmp9Q!/b/dG4BAAAAAAAA&bo=wAMABcADAAURCT4!&rf=viewer_4
# #
# # http://b269.photo.store.qq.com/psb?/V13Api2e4EkLWV/iUZ7AyvPKle1FEfDtPW2ALtzbSs6eYuKrLDX13*KkoQ!/m/dA0BAAAAAAAAnull&bo=AAW.BjAMcBARCd8!&rf=photolist&t=5
# # http://b269.photo.store.qq.com/psb?/V13Api2e4EkLWV/iUZ7AyvPKle1FEfDtPW2ALtzbSs6eYuKrLDX13*KkoQ!/b/dA0BAAAAAAAA&bo=AAW.BjAMcBARCd8!&rf=viewer_4
# # http://r.photo.store.qq.com/psb?/V13Api2e4EkLWV/iUZ7AyvPKle1FEfDtPW2ALtzbSs6eYuKrLDX13*KkoQ!/r/dA0BAAAAAAAA
# #
# # b[1~9] = r
# # /m/ = r
# #
# # app_canvas_frame xh-highlight