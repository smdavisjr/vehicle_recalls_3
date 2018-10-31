import requests
import json

url = "https://one.nhtsa.gov/webapi//api/Recalls/vehicle/modelyear/2015/make/infiniti/model/q50?format=json"
recall_url_data = (requests.get(url)).text
json_data = json.loads(recall_url_data)
json_str = json.dumps(json_data)
json_dict = json.loads(json_str)

for key in json_dict:
    count_recalls = json_dict['Count']
print('')
print('Number of Recalls Found: ', count_recalls)
print('==========')

for Results in json_dict['Results']:
    print('')
    print('---')
    print('Component: ', Results['Component'])
    print('Concequence: ', Results['Conequence'])
    print('NHTSA Campaign Number: ', Results['NHTSACampaignNumber'])
    print('Recall Webpage: ', 'https://www.nhtsa.gov/recalls?nhtsaId=' + Results['NHTSACampaignNumber'])
    # print('Recall Sumary: ', Results['Summary'])
print('==========')
print('')


# for key in json_dict:
    # count_recalls = resp['Count']
    # result_output_0 = (count_recalls - (count_recalls - 1))
    # result_output_add1 = result_output_0 + 1
    # print(result_output_0)
    # print(result_output_add1)

    # recall_component = resp['Results'][int(result_output_add1)]['Component']
    # print(recall_component)
