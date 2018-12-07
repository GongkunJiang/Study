from selenium.webdriver import Chrome, ActionChains
from selenium.webdriver.support.ui import Select
import time


class UserData:
    def __init__(self, user):
        self.name = user.text
        self.url = user.get_attribute('href')


if __name__ == '__main__':
    driver = Chrome()
    url = "https://s.weibo.com/user?"
    driver.get(url)
    # 选择地区
    driver.find_element_by_xpath('//*[@id="pl_user_filtertab"]/div[1]/ul/li[1]/span').click()
    driver.find_element_by_link_text('重庆').click()
    driver.find_element_by_link_text('所有').click()
    # 选择用户
    ac = driver.find_element_by_xpath('//*[@id="pl_user_filtertab"]/div[1]/ul/li[2]/span')
    ActionChains(driver).move_to_element(ac).perform()
    driver.find_element_by_link_text('普通用户').click()
    # 选择性别
    ac = driver.find_element_by_xpath('//*[@id="pl_user_filtertab"]/div[1]/ul/li[3]/span')
    ActionChains(driver).move_to_element(ac).perform()
    driver.find_element_by_link_text('女').click()
    # 选择年龄
    ac = driver.find_element_by_xpath('//*[@id="pl_user_filtertab"]/div[1]/ul/li[4]/span')
    ActionChains(driver).move_to_element(ac).perform()
    driver.find_element_by_link_text('不限').click()
    print(driver.current_url)

    users = driver.find_elements_by_xpath('//*[@id="pl_user_feedList"]/div/div[2]/div/a[1]')
    dynamic = []
    spider = [UserData(user) for user in users]
    for user in spider:
        driver.get(user.url)
        time.sleep(5)
        datas = driver.find_elements_by_xpath(
            '//*[contains(@id,"Pl_Official_MyProfileFeed")]/div/div/div[1]/div[3]/div[4]')
        for data in datas:
            index = datas.index(data) + 1
            dm = user.name  + '[%d]: '%index + data.text.strip().replace('\n', ' ')
            print(dm)
            dynamic.append(dm)
