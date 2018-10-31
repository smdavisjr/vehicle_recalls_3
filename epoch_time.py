import time
import json

with open('q50_recalls.json') as file:
    data = json.load(file)
json_str = json.dumps(data)
resp = json.loads(json_str)

for Results in resp['Results']:
    recall_date = int(Results['ReportReceivedDate'][6:16])
    # print(recall_date)
    timestamp = time.strftime("%B %d, %Y", time.localtime(recall_date))
    print (timestamp)
