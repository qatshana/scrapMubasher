from selenium import webdriver
#driver = webdriver.Firefox(executable_path=r'C:\Users\aqatshan\geckodriver.exe')

browser=webdriver.Firefox(executable_path=r'C:\Users\aqatshan\geckodriver.exe')
browser.get('http://www.duckduckgo.com')
searchResult=browser.find_element_by_id("search_form_input_homepage")
searchResult.send_keys('real python')
searchResult.submit()

results=searchResult.find_elements_by_class_name('result')

print (results)


browser.close()
