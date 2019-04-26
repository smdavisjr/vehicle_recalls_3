# 2015 Infiniti Q50 JN1BV7AP9FM341979
# 2015 Lincoln MKZ 3LN6L2G99FR621162

import requests
# import json
# import re
# import csv

vin = input("Enter vehicle(s) VIN separated by semicolons: ")
# vin = str(vin)
url = 'https://vpic.nhtsa.dot.gov/api/vehicles/DecodeVINValuesBatch/'
post_fields = {'format':json, 'data':vin}
results = requests.post(url, data=post_fields)
raw_data = rsults.json
print(raw_data)

# print(re.sub('([":"])', r' \1', raw_data))
#
# split = results.split(':')
# print(split)

# colon = ':'
# result = ''
# for colon in raw_data:
#     refined_data = result + colon + ' '
# print (refined_data)
# d = json.loads(r)
# print d['count']

# json_str = json.dumps(raw_data, separators=(',',':'))
# resp = json.loads(json_str)
# print(json_str, sort_keys=True, indent=4)
# print(json.dumps(raw_data, indent=2))


# test1 = str(resp(['Results']['AirBagLocCurtain']))
# print(test1)

# for 'Message' in resp:
    # test1 = str(resp[key]['Results']['AirBagLocCurtain'])
    # test1 = [0][0]
# print(test1)

# stringify
