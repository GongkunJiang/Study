from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# driver = webdriver.Edge()
# driver = webdriver.Chrome()
from selenium.webdriver.edge.options import Options
# mobile_emulation = {
#     "deviceMetrics": { "width": 360, "height": 640, "pixelRatio": 3.0 },
#     "userAgent": "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1"
# }
options = Options()
# options.add_experimental_option("mobileEmulation", mobile_emulation)
# prefs = {"profile.managed_default_content_settings.images": 2} # 禁止加载图片
# options.add_experimental_option("prefs", prefs)
options.add_experimental_option("prefs", {"profile.managed_default_content_settings.javascript": 2})
#当HTML被接收到浏览器时，`get()`就完成了，无需等待解析页面
# options.page_load_strategy = 'none'
# options.headless = True
driver = webdriver.Edge(options=options)
# url = "https://www.zongcaixiaoshuow.com/qing/1940/798730.html"
# url = "https://m.biqooge.com/13_13497/8566154.html"
# url = "https://www.biqooge.com/13_13418/8514277.html"
url = "http://wap.biqugeai.com/18/18208/9713202.html"
driver.get(url)
# driver.execute_script("var stylesheets = document.styleSheets; for(var i=0; i<stylesheets.length; i++){stylesheets[i].disabled=true;}")
try:
	info = driver.find_element(By.CLASS_NAME,'panel-heading')
	name = info.find_element(By.TAG_NAME,'a').text
	author = info.find_element(By.TAG_NAME,'p').text[3:]
except Exception as e:
	try:
		info = driver.find_element(By.NAME,'keywords').get_attribute("content").split(",")
		name = info[0]
		author = info[1][:-2]
	except Exception as e:
		info = driver.find_element(By.NAME,'description').get_attribute("content")
		name = info.split("《")[1].split("》")[0]
		author = info.split("提供了")[1].split("创作的")[0]
	
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
r"『添加到书签』"
]
title = ""
flag=1
with open(book, "w",  encoding='utf-8') as f:
	while flag:
		try:
			try:
				tmp = driver.find_element(By.CLASS_NAME,'panel-footer').text
			except Exception as e:
				try:
					tmp = driver.find_element(By.CLASS_NAME,'title').text
				except:
					# tmp = title
					tmp = driver.find_element(By.NAME,'keywords').get_attribute("content").split(",")[-1]
			if title != tmp:
				title = tmp
				print(title, "write title", end="\t")
				f.write(title)
				f.write("\n")
			time.sleep(0.5)
			if "google_vignette" not in driver.current_url:
				try:
					content = driver.find_element(By.ID,'content').text
				except Exception as e:
					try:
						content = driver.find_element(By.ID,'chaptercontent').text
					except Exception as e:
						content = driver.find_element(By.ID,'booktxt').text
				print(driver.title, "write content")
				for ad in ads:
					content = content.replace(ad, "")
				f.write(content.replace("\n\n", "\n"))
				f.write("\n")
			
			# next_page = driver.find_elements(By.CLASS_NAME,'sub-title')[-1]
			# next_page.find_element(By.PARTIAL_LINK_TEXT, '').click()
			next_page = driver.find_element(By.PARTIAL_LINK_TEXT, '下一')
			tmp = next_page.get_attribute("href")
			if tmp and (tmp not in driver.current_url):
				next_page.click()
			else:
				flag = 0
			
		except Exception as r:
			print("HIT Exception", r)
			time.sleep(5)
		# break
