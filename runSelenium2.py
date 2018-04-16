from selenium import webdriver
from time import sleep
#driver = webdriver.Firefox(executable_path=r'C:\Users\aqatshan\geckodriver.exe')
ur='https://www.tadawul.com.sa/wps/portal/tadawul/markets/equities/market-watch'
browser=webdriver.Firefox(executable_path=r'C:\Users\aqatshan\geckodriver.exe')
#browser.get('http://www.duckduckgo.com')
browser.get(ur)
#searchResult=browser.find_element_by_id("search_form_input_homepage")
#searchResult.send_keys('real python')
#searchResult.submit()

#results=searchResult.find_elements_by_class_name('result')
sleep(10)

data=browser.page_source

print(browser.page_source)

#print (results)


browser.close()

f=open('temp.html','w')

f.write(data)

f.close()
