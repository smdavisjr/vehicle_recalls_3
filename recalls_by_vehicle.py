# import requests

while True:
	try:
		year_int = int(raw_input("Enter vehincle year: "))
	except ValueError:
		print("Please enter a number for the vehicle year.")
		continue
	else:
		break

while True:
	make = str(raw_input("Enter vehicle make: "))
	if make.isalpha() is False:
		print("Make must only contain alphanumeric characters and cannot be left blank.")
	else:
		break

while True:
	model = str(raw_input("Enter vehicle model: "))
	if model.isalnum() is False:
		print("Model must be alphanumeric and cannot be blank.")
	else:
		break

year_str = str(year_int)
url = "https://one.nhtsa.gov/webapi//api/Recalls/vehicle/modelyear/" + year_str + "/make/" + make + "/model/" + model + "?format=json"

import webbrowser
webbrowser.open(url)
