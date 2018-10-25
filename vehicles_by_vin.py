import requests
import json;
vin = input("Enter vehicle(s) VIN separated by semicolons: ")
url = 'https://vpic.nhtsa.dot.gov/api/vehicles/DecodeVINValuesBatch/';
post_fields = {'format': 'json', 'data':vin};
r = requests.post(url, data=post_fields);
print(r.text);
