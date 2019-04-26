# 2015 Infiniti Q50 JN1BV7AP9FM341979
# 2015 Lincoln MKZ 3LN6L2G99FR621162
# Both VIN: JN1BV7AP9FM341979;3LN6L2G99FR621162

import requests
import json
import webbrowser

# vin = input("Enter vehicle(s) VIN separated by semicolons: ")
vin = input('Enter vehicle VIN: ')
url = 'https://vpic.nhtsa.dot.gov/api/vehicles/DecodeVINValuesBatch/'
post_fields = {'format': 'json', 'data':vin}
results = requests.post(url, data=post_fields)
raw_data = results.text
json_data = json.loads(raw_data)
json_str = json.dumps(json_data)
resp1 = json.loads(json_str)

for key in resp1:
    num_vehicles = resp1['Count']
    # year = resp['Results'][0]['ModelYear']
    # make = resp['Results'][0]['Make']
    # model = resp['Results'][0]['Model']

print('')
print('==========')
print('Number of Matches:', num_vehicles)

for Results in resp1['Results']:
    year = Results['ModelYear']
    make = Results['Make']
    model = Results['Model']
    print('Year:', year)
    print('Make:', make)
    print('Model:', model)
    print('-----')
print('==========')

url = "https://one.nhtsa.gov/webapi//api/Recalls/vehicle/modelyear/" + year + "/make/" + make + "/model/" + model + "?format=json"
recall_url_data = (requests.get(url)).text
json_data = json.loads(recall_url_data)
json_str = json.dumps(json_data)
resp2 = json.loads(json_str)

for key in resp2:
    count_recalls = resp2['Count']
    print('Number of Recalls Found for', year, make, model, ': ', count_recalls)
    break
print('==========')
print('')


while True:
    view_recalls_terminal = input('View Recall Summary? (Yes/No): ')
    print('')
    if view_recalls_terminal == 'Yes' or view_recalls_terminal == 'yes':
        print('==========')
        print('')
        for Results in resp['Results']:
            print('Component: ', Results['Component'])
            print('Concequence: ', Results['Conequence'])
            print('NHTSA Campaign Number: ', Results['NHTSACampaignNumber'])
            print('Recall Webpage: ', 'https://www.nhtsa.gov/recalls?nhtsaId=' + Results['NHTSACampaignNumber'])
            print('')
            print('')
        break
    elif view_recalls_terminal == 'No' or view_recalls_terminal == 'no':
        print('SUMMARY NOT REQUESTED')
        print('')
        break
    else:
        print('')
        print('Please type "Yes" or "No"')
        print('')

print('==========')
print('END')
print('==========')
print('')




# while True:
#     open_url = input('View Recalls in Browser? (Yes/No): ')
#     if open_url == 'Yes' or open_url == 'yes':
#         webbrowser.open(url)
#         print('')
#         print('Recalls Successfully Loaded in Browser')
#         print('')
#         break
#     if open_url == 'No' or open_url == 'no':
#         print('')
#         print('Browser Not Loaded')
#         print('')
#         break
#     else:
#         print('')
#         print('Please type "Yes" or "No"')
#         print('')
