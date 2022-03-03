import requests
import json

baseUrl = 'https://api.opensea.io/api/v1/'

def get_collection(collection: str):
	response = requests.get(baseUrl + 'collection/' + collection)
	json_text = json.loads(response.text)
	return json_text['collection']['stats']['floor_price']
