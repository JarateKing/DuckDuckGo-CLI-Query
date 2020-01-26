import requests
import sys
import json

args = '+'.join(sys.argv[1:])
response = requests.get("https://api.duckduckgo.com/?q=" + args + "&format=json")

if (response.status_code == 200):
	values = response.json()
	if (len(values['AbstractText']) > 0):
		print(values['AbstractText'])
else:
	print("error: ", response.status_code)

