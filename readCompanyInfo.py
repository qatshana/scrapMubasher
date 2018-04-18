import json

ticker='4011'
fname=ticker+'-FullData.json'

with open(fname, "r") as fr:
	data=fr.read()

dictData=json.loads(data)

print (dictData['Description'])

print (dictData['Market Stats']['Previous Close'])

print (dictData['P/B Ratio'])

print (dictData['Market Cap'])