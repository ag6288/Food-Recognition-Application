import pandas as pd
import numpy as np
import json

def lambda_handler(event, context):
	data = pd.read_csv('data.csv')
	label = event['params']['querystring']['food']
	print("food_item = ", label)
	df = data.loc[data[label] == 1, ['restaurant', 'lat', 'lon', 'address', 'contact']]
	restaurant = df['restaurant'].tolist()
	lat = df['lat'].tolist()
	lon = df['lon'].tolist()
	address = df['address'].tolist()
	contact = df['contact'].tolist()
	results = {'restaurant':restaurant, 'lat':lat, 'lon':lon, 'address':address, 'contact':contact}
	print("results = ", results)
	return json.dumps({'results': results})