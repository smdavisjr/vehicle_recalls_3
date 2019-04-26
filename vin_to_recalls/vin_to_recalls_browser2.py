# 2015 Infiniti Q50 JN1BV7AP9FM341979
# 2015 Lincoln MKZ 3LN6L2G99FR621162
# Both VIN: JN1BV7AP9FM341979;3LN6L2G99FR621162

import requests
import json
import webbrowser

# vin = input("Enter vehicle(s) VIN separated by semicolons: ")
vin = input("Enter vehicle VIN: ")
url = 'https://vpic.nhtsa.dot.gov/api/vehicles/DecodeVINValuesBatch/'
post_fields = {'format': 'json', 'data':vin}
results = requests.post(url, data=post_fields)
raw_data = results.text
json_data = json.loads(raw_data)
json_str = json.dumps(json_data)
resp = json.loads(json_str)
for key in resp:
    num_vehicles = resp['Count']
    year = resp['Results'][0]['ModelYear']
    make = resp['Results'][0]['Make']
    model = resp['Results'][0]['Model']

print('-----')
# print('Number of Vehicles Returned:', num_vehicles)
print('Year:', year)
print('Make:', make)
print('Model:', model)
print('-----')


url = "https://one.nhtsa.gov/webapi//api/Recalls/vehicle/modelyear/" + year + "/make/" + make + "/model/" + model + "?format=json"
recall_url_data = (requests.get(url)).text
json_data = json.loads(recall_url_data)
json_str = json.dumps(json_data)
resp = json.loads(json_str)
for key in resp:
    count_recalls = resp['Count']
print("Number of Recalls Found:", count_recalls)
print('-----')


open_url = input("Open Browser to View Recalls? (Yes/No): ")
if open_url == 'Yes' or open_url == 'yes':
    webbrowser.open(url)
    print("Recalls Successfully Loaded in Browser")
elif open_url == 'No' or open_url == 'no':
    print("Browser Not Loaded")
else:
    print("Please re-run program and type 'Yes' or 'No'")
