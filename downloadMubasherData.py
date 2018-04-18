from selenium import webdriver
from time import sleep
import io

def dowloadTasiStocks(fname,ur):	
	browser=webdriver.Firefox(executable_path=r'C:\Users\qatsh\geckodriver.exe')
	browser.get(ur)
	sleep(30)
	data=browser.page_source
	browser.close()
	with io.open(fname, "w", encoding="utf-8") as f:
	    f.write(data)

if __name__ == "__main__":
	ticker='4011'
	fname=ticker+'-Profile.html'
	ur='https://english.mubasher.info/markets/TDWL/stocks/'+ticker+'/profile'
	dowloadTasiStocks(fname,ur)
	
	fname=ticker+'-Stock.html'
	ur='https://english.mubasher.info/markets/TDWL/stocks/'+ticker
	dowloadTasiStocks(fname,ur)
