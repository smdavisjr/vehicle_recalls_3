# 2015 Infiniti Q50 JN1BV7AP9FM341979
# 2015 Lincoln MKZ 3LN6L2G99FR621162
# Both VIN: JN1BV7AP9FM341979;3LN6L2G99FR621162

import requests
import json
import time

vin = input("Enter vehicle(s) VIN separated by semicolons: ")
url = 'https://vpic.nhtsa.dot.gov/api/vehicles/DecodeVINValuesBatch/'
post_fields = {'format': 'json', 'data':vin}
results = requests.post(url, data=post_fields)
raw_data = results.text
json_data = json.loads(raw_data)
json_str = json.dumps(json_data)
resp1 = json.loads(json_str)

for key in resp1:
    num_vehicles = resp1['Count']

print('')
print('Number of Results Returned:', num_vehicles)
print('========================================')
print('')

for Results in resp1['Results']:
    print('========================================')
    print('VEHICLE INFORMATION')
    year = Results['ModelYear']
    make = Results['Make']
    model = Results['Model']
    url = "https://one.nhtsa.gov/webapi//api/Recalls/vehicle/modelyear/" + year + "/make/" + make + "/model/" + model + "?format=json"
    recall_url_data = (requests.get(url)).text
    json_data = json.loads(recall_url_data)
    json_str = json.dumps(json_data)
    resp2 = json.loads(json_str)
    print('Year:', year)
    print('Make:', make)
    print('Model:', model)
    print('')

    for key in resp2:
        count_recalls = resp2['Count']
        print('Number of Recalls Found for', '"',year, make, model,'"', ':', count_recalls)
        print('========================================')
        break
    print('')

    while True:
        print("View Recall Summary for", year, make, model, "?")
        view_recalls_terminal = input('(Yes/No): ')
        print('')
        if view_recalls_terminal == 'Yes' or view_recalls_terminal == 'yes':
            print('========================================')
            print('')
            for Results in resp2['Results']:
                recall_date = int(Results['ReportReceivedDate'][6:16])
                print('Date: ', time.strftime("%B %d, %Y", time.localtime(recall_date)))
                print('Component: ', Results['Component'])
                print('Concequence: ', Results['Conequence'])
                print('NHTSA Campaign Number: ', Results['NHTSACampaignNumber'])
                print('Recall Webpage: ', 'https://www.nhtsa.gov/recalls?nhtsaId=' + Results['NHTSACampaignNumber'])
                print('')
                print('')
            break
        elif view_recalls_terminal == 'No' or view_recalls_terminal == 'no':
            print('SUMMARY NOT REQUESTED')
            print('========================================')
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
