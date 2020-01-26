import requests
import sys
import json

query = 'what+is+' + ('+'.join(sys.argv[1:]))
response = requests.get("https://api.duckduckgo.com/?q=" + query + "&format=json")

if (response.status_code == 200):
	values = response.json()
	if (len(values['AbstractText']) > 0):
		print(values['AbstractText'])
else:
	print("error: ", response.status_code)
