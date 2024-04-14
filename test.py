# https://tieba.baidu.com/p/5575891471?pn=1
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# driver = webdriver.Chrome()
from selenium.webdriver.edge.options import Options
options = Options()
mobile_emulation = {
    "deviceMetrics": { "width": 360, "height": 640, "pixelRatio": 3.0 },
    "userAgent": "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1"
}
options.add_experimental_option("mobileEmulation", mobile_emulation)
prefs = {"profile.managed_default_content_settings.images": 2} # 禁止加载图片
options.add_experimental_option("prefs", prefs)
# prefs = {"profile.managed_default_content_settings.javascript": 2} # 禁用jsp
# options.add_experimental_option("prefs", prefs)
# 当HTML被接收到浏览器时，`get()`就完成了，无需等待解析页面
# options.page_load_strategy = 'none'
# options.headless = True
driver = webdriver.Edge(options=options)
# url = "https://www.zongcaixiaoshuow.com/qing/1940/798730.html"
# url = "https://www.biqooge.com/13_13419/8514384.html"
# url = "http://wap.biqugeai.com/18/18208/9713202.html"
# url = "https://www.xixiwx.net/read/8012/3246797.html"
# url = "https://www.ckxxbz.com/book/zailianbushu/566255.html"
# url = "https://www.yanqingla.com/heibai/uJeruKV7uqxx0vLUPabV.html"
# url = "https://m.beqege.cc/55463/739501.html"
# url = "https://m.biqugeli.com/book/47431/13192178.html"
# url = "https://www.tcknh.com/chapter/35722/71445.html"
# url = "https://www.wduec.com/82243/32714350.html"
# url = "https://m.tiaobiquge.com/123190/1436537.html"
url = "https://xs30238.top/v3_uni_0414140?1#/v3/46664377/1962065/1.html"
# url = "https://8115b.bi17.cc/html/70444/1.html"
# url = "https://www.xuges.com/yq/q/qc/yyl/001.htm"
# url = "https://www.dingdian-xiaoshuo.com/n/yinyongfengge/21931.html"
# url = "https://www.msfuer.com/book/8677/4810233.html"

driver.get(url)
driver.execute_script("var stylesheets = document.styleSheets; for(var i=0; i<stylesheets.length; i++){stylesheets[i].disabled=true;}") # 禁用CCS

# try:
# 	info = driver.find_element(By.CLASS_NAME,'panel-heading')
# 	name = info.find_element(By.TAG_NAME,'a').text
# 	author = info.find_element(By.TAG_NAME,'p').text[3:]
# except Exception as e:
# 	info = driver.find_element(By.NAME,'keywords').get_attribute("content").split(",")
# 	name = info[1]
# 	author = info[2]#[:-2]

	# info = driver.find_element(By.NAME,'description').get_attribute("content")
	# name = info.split("《")[1].split("》")[0]
	# try:
	# 	author = info.split("提供了")[1].split("创作的")[0]
	# except:
	# 	author = info.split("整理")[1].split("的小说")[0]

name = "盗情"
author = "周玉"
book=fr"C:\小说\{name}_{author}.txt"
print(book)

ads = [r"【精武小说网将分享完结好看的言情小说以及耽美小说等，找好看的小说就来精武小说网https://.25645/】", 
r"『点此章节报错』", 
r"附：本书籍仅供学习jiāo流之用，请在下载后24小时内自行删除", 
r"【告知苹果书友，以后能免费稳定看书的网站、app只会更少，站长推荐赶快安装一个专为苹果书友打造的听书，换源，找书都很棒的换源APP，解决书荒不迷路！】", 
r"【告知安卓书友，越来越多免费站点将会关闭失效，安卓app鱼目混珠，找一个安全稳定看书的app非常有必要，站长强烈推荐换源APP，听书、换源、找书超好使！】", 
r"【告知书友，越来越多免费站点将会关闭失效，安卓app鱼目混珠，找一个安全稳定看书的app非常有必要，站长强烈推荐换源APP，听书、换源、找书超好使！】",
r"【告知书友，时代在变化，免费站点难以长存，手机app多书源站点切换看书大势所趋，站长给你推荐的这个换源APP，听书音色多、换源、找书都好使！】",
r"↗傻↗逼↗小↗说,www.shabixiaoshuo.im ”", 
r"↑傻↑逼↑小↑说,www.shabixiaoshuo.im ”", 
r"★傻★逼★小★说,www.shabixiaoshuo.im ”", 
r"→傻→逼→小→说,www.shabixiaoshuo.im ”", 
r"◢傻◢逼◢小◢说,www.shabixiaoshuo.im ”", 
r"▅傻▅逼▅小▅说,www.shabixiaoshuo.im ”", 
r"◆傻◆逼◆小◆说,www.shabixiaoshuo.im ”", 
r"请收藏：https://m.bi17.cc", 
r"请收藏：https://m.biqg.cc", 
r"（温馨提示：请关闭畅读或阅读模式，否则内容无法正常显示）", 
r"阅读本小说最新章节请到黄金书屋www.360118.com", 
r"她名曰月白白眉眼如月是月家的七小姐。wwW.360118.COM", 
r"wwW.360118.CoM", 
r"『添加到书签』"
]
title = ""
flag=1
with open(book, "w",  encoding='utf-8') as f:
	while flag:
		try:
			# try:
			# 	# tmp = driver.find_element(By.CLASS_NAME,'panel-footer').text
			# 	tmp = driver.find_element(By.CLASS_NAME,'title').text
			# 	# tmp = driver.find_element(By.CLASS_NAME,'bookname').find_element(By.TAG_NAME,'h1').text
			# except Exception as e:
			# 	# tmp = title
			# 	tmp = driver.find_element(By.NAME,'keywords').get_attribute("content").split(",")[-1]
			# 	# tmp = driver.find_element(By.XPATH,"/html/body/div/div[2]/div[1]/h2").text
						#	
			# if title != tmp:
			# 	title = tmp
			# 	print(title, "write title", end="\t")
			# 	f.write(title)
			# 	f.write("\n")
			time.sleep(0.5)
			if "google_vignette" not in driver.current_url:
				content = driver.find_element(By.ID,'nr1').text
				# content = driver.find_element(By.ID,'article').text
				# content = driver.find_element(By.ID,'txt').text
				# content = driver.find_element(By.ID,'booktxt').text
				# content = driver.find_element(By.ID,'content').text
				# content = driver.find_element(By.ID,'chaptercontent').text
				# content = driver.find_element(By.CLASS_NAME,'newstext').text
				# content = driver.find_element(By.XPATH, "/html/body/div[3]/table/tbody/tr[4]").text
				
				print(title, "write content")
				for ad in ads:
					content = content.replace(ad, "")
				f.write(content.replace("\n\n", "\n"))
				f.write("\n")
			

			# next_page.find_element(By.PARTIAL_LINK_TEXT, '').click()
			try:
				# next_page = driver.find_elements(By.CLASS_NAME,'sub-title')[-1]
				next_page = driver.find_elements(By.CLASS_NAME,'next')[-1]
				# if "下一" not in next_page.text:
				# 	flag = 0
				next_page = next_page.find_element(By.TAG_NAME,'a')
				
				# next_page = driver.find_element(By.PARTIAL_LINK_TEXT, '下一')
				# next_page = driver.find_elements(By.PARTIAL_LINK_TEXT, '章')[-1]
				tmp = next_page.get_attribute("href")
				# if flag and tmp and (tmp not in driver.current_url):
				if flag and tmp and (tmp[-1] != "/") and (tmp[-9:] != "index.htm"):
					# next_page.click()
					print(tmp)
					driver.get(tmp)
				else:
					flag = 0
			except Exception as e:
				flag = 0
			
		except Exception as e:
			print("HIT Exception", e)
			time.sleep(5)
		# break
