# 2015 Infiniti Q50 JN1BV7AP9FM341979
# 2015 Lincoln MKZ 3LN6L2G99FR621162

import requests
import json

vin = input("Enter vehicle(s) VIN separated by semicolons: ")
url = 'https://vpic.nhtsa.dot.gov/api/vehicles/DecodeVINValuesBatch/'
post_fields = {'format': 'json', 'data':vin}
results = requests.post(url, data=post_fields)
raw_data = results.text
json_data = json.loads(raw_data)
json_str = json.dumps(json_data)
resp = json.loads(json_str)
# print(resp)

for key in resp:
    num_vehicles = resp['Count']
    year = resp['Results'][0]['ModelYear']
    make = resp['Results'][0]['Make']
    model = resp['Results'][0]['Model']

print('-----')
print('Number of Vehicles Returned:', num_vehicles)
print('Year:', year)
print('Make:', make)
print('Model:', model)
print('-----')
