import json

fname='SAMBA-FullData.json'

with open(fname, "r") as fr:
	data=fr.read()

dictData=json.loads(data)

print (dictData['Description'])

print (dictData['Market Stats']['Previous Close'])

print (dictData['P/B Ratio'])
