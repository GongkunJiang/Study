from selenium.webdriver import Chrome, ActionChains
from selenium.webdriver.support.ui import Select
import time, requests, os

driver = Chrome()
# url = "https://www.duitang.com/album/?id=73158879"
url = 'https://www.duitang.com/album/?id=71117322'
driver.get(url)
figs = driver.find_elements_by_xpath('//*[@id="woo-holder"]/div[2]/div[2]/div/div/div[1]/a/img')
path = r'C:\Users\Administrator.YLMF-20150729SV\Desktop\DT'
for fig in figs:
    index = figs.index(fig)
    # if index < 9:
    url = fig.get_attribute('src').replace('.thumb.224_0', '')
    name = url[-25:]
    data = requests.Session().get(url, headers={"User-Agent": "Mozilla/5.0"}).content
    if not os.path.exists(path):
        os.makedirs(path)
    with open('%s/%s.jpg' % (path, name), 'wb') as f:
        f.write(data)
#     print('Save done\t' + name)



print("helloworld")

# 文件批量改名
# import os
#
# path = r'C:\Users\Administrator.YLMF-20150729SV\Desktop\DT'
#
# # 获取该目录下所有文件，存入列表中
# f = os.listdir(path)
#
# n = 0
# for i in f:
#     # 设置旧文件名（就是路径+文件名）
#     oldname = path + '\\' + f[n]
#
#     # 设置新文件名
#     newname = path + '\\' + f[n][:-4]
#
#     # 用os模块中的rename方法对文件改名
#     os.rename(oldname, newname)
#     print(oldname, '======>', newname)
#
#     n += 1
