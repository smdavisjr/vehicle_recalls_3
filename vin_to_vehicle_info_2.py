import json

with open('Q50_vin_output.json') as file:
# with open('Q50_vin_output_unformatted.json') as file:
# with open('Q50_vin_output_unformatted.txt') as file:
    data = json.load(file)
json_str = json.dumps(data, sort_keys=True, indent=2)
resp = json.loads(json_str)
# print(json_str)

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
