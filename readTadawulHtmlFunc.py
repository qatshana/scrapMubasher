from bs4 import BeautifulSoup
import pandas as pd
import json

from selenium import webdriver
from time import sleep
import io



'''
fRead='test2.html'
f=open(fRead,'r')

data=f.read()

f.close()


soup = BeautifulSoup(data,'html')

'''


def readFile(fname):
	with open(fname,'r') as fr:
		data=fr.read()	
	soup = BeautifulSoup(data)
	return soup	

def readHteml(group,soup):	
	

	Lmod=[]
	rowsGeneral= soup.findAll('tr', {'class': group})
	for m in rowsGeneral:
		d=m.text
		Lmod.append(d.strip().split('\n'))
	return (Lmod)	


def getDFStockPrices(groups,fname):
	soup=readFile(fname)
	stockList=[]
	for group in groups:
		stockList.append(readHteml(group,soup))
	data=[]
	for group in stockList:
		for line in group:
			data.append(line)
	stockPrices=pd.DataFrame(data)	
	return stockPrices

def getDfStockPricesAll(fname):
	groups=["odd group-item group-item-energy","even group-item group-item-energy",\
		"odd group-item group-item-materials","even group-item group-item-materials",\
		"odd group-item group-item-capital-goods","even group-item group-item-capital-goods",\
		"odd group-item group-item-commercial-amp-professional-svc","even group-item group-item-commercial-amp-professional-svc",\
		"odd group-item group-item-transportation","even group-item group-item-transportation"\
		"odd group-item group-item-consumer-durables-amp-apparel","even group-item group-item-consumer-durables-amp-apparel",\
		"odd group-item group-item-consumer-services","even group-item group-item-consumer-services",
		"odd group-item group-item-media","even group-item group-item-media",\
		"odd group-item group-item-retailing","even group-item group-item-retailing",\
		"odd group-item group-item-food-amp-staples-retailing","even group-item group-item-food-amp-staples-retailing",\
		"odd group-item group-item-food-amp-beverages","even group-item group-item-food-amp-beverages",
		"odd group-item group-item-health-care-equipment-amp-svc","even group-item group-item-health-care-equipment-amp-svc",\
		"odd group-item group-item-pharma-biotech-amp-life-science","even group-item group-item-pharma-biotech-amp-life-science",\
		"odd group-item group-item-banks" ,"even group-item group-item-banks",\
		"odd group-item group-item-diversified-financials","even group-item group-item-diversified-financials",\
		"odd group-item group-item-insurance","even group-item group-item-insurance",\
		"odd group-item group-item-telecommunication-services","even group-item group-item-telecommunication-services",\
		"odd group-item group-item-utilities","even group-item group-item-utilities",\
		"odd group-item group-item-reits","even group-item group-item-reits",\
		"odd group-item group-item-real-estate-mgmt-amp-dev-t","even group-item group-item-real-estate-mgmt-amp-dev-t"]
	return getDFStockPrices(groups,fname)


def genStockCsc(file,fr):
	df=getDfStockPricesAll(fr)
	with open(file,'w') as fw:
		df.to_csv(fw,index=False)		



def dowloadTasiStocks(fname):
	ur='https://www.tadawul.com.sa/wps/portal/tadawul/markets/equities/market-watch'
	browser=webdriver.Firefox(executable_path=r'C:\Users\aqatshan\geckodriver.exe')
	browser.get(ur)
	sleep(10)
	data=browser.page_source
	browser.close()
	with io.open(fname, "w", encoding="utf-8") as f:
	    f.write(data)

if __name__ == "__main__":
	#fname='test2.html'
	#dowloadTasiStocks(fname)
	fr='test2.html'
	file="stocks6.csv"
	genStockCsc(file,fr)
