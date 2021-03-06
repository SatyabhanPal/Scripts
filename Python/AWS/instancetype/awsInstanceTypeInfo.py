import csv
import json
import requests
awsEc2IndexUrl='https://pricing.us-east-1.amazonaws.com/offers/v1.0/aws/AmazonEC2/current/index.csv'
fileName='awsIndex.csv'
print ("Downloading the index.json file...")
r = requests.get(awsEc2IndexUrl, stream=True)
if(r.status_code != 200):
	print ("Failed to get the data from AWS")
	exit()
with open(fileName,'wb') as fw:
	fw.write(r.content)

data="".join(open(fileName).readlines()[5:-1])
open(fileName,"w").write(data)
with open (fileName) as fh:
	reader=csv.DictReader(fh)
	instanceTypeDict=[]
	for row in reader:
		tempDict={}
		if row['Tenancy']=='Shared' and row['Operating System']=='Linux' and row['Location']=='US West (N. California)' and row['TermType']=='OnDemand':
			tempDict[row['Instance Type']]={
									'vCPU':row['vCPU'],
									'Physical Processor':row['Physical Processor'],
									'Clock Speed':row['Clock Speed'],
									'Memory':row['Memory'],
									'Storage':row['Storage'],
									'Processor Architecture':row['Processor Architecture'],
									'Network Performance':row['Network Performance']
									}
			instanceTypeDict.insert(0,tempDict)
print (json.dumps(instanceTypeDict,indent=4, sort_keys=True))