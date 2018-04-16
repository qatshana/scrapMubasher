from bs4 import BeautifulSoup
import pandas as pd
import json

f=open('tadawulHTML.html','r')

data=f.read()

soup = BeautifulSoup(data,'html')


def readHteml(group):	

	Lmod=[]
	rowsGeneral= soup.findAll('tr', {'class': group})
	for m in rowsGeneral:
		d=m.text
		Lmod.append(d.strip().split('\n'))
	return (Lmod)	


def getDFStockPrices(groups):
	stockList=[]
	for group in groups:
		stockList.append(readHteml(group))
	data=[]
	for group in stockList:
		for line in group:
			data.append(line)
	stockPrices=pd.DataFrame(data)	
	return stockPrices

def getDfStockPricesAll():
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
	return getDFStockPrices(groups)


def genStockCsc(file):
	df=getDfStockPricesAll()
	with open(file,'w') as fw:
		df.to_csv(fw,index=False)		


if __name__ == "__main__":
	file="stocks2.csv"
	genStockCsc(file)
