import rauth
import requests
from pprint import pprint
import json

# Comment out main file at the bottom to test if it works
# in the terminal run 'python yelp_client'
# should write out json into data.json 

keys = {
	'CONSUMER_KEY': '3KcyyCeF3C1EzYV9Vdy1Lw',
	'CONSUMER_SECRET': 'snYRK3XtH1sOgJfE_8jSgA87Hrc',
	'TOKEN': 'SUyn4b1-la_pvrngf_HIhjiLiwdTDrY3',
	'TOKEN_SECRET': 'QBXSiN0Eqsaq-Xc5o0-MpVT03r4',
}

webapp_url = "http://127.0.0.1:8000"
api_post_url = "/v1/restaurants/"


class YelpClient(object):

	def get_all_sets(self, key, limit):
		# PRE: keys: dictionary of yelp keys; limit: how many data points do you want
		# POST: nothing
		# RETURNS: JSON data containing all the data points
		data = self._get_single_data_set(keys, 0)
		for i in range(20, limit, 20):
			next_set = self._get_single_data_set(keys, i)
			data[u'businesses'].extend(next_set[u'businesses'])
		return data


	def _get_single_data_set(self, keys, offset):
		# PRE: keys: dictionary of yelp keys; 
		#	   offset: the next n set of data points we want (each set in 20 data points big)
		# POST: nothing 
		# RETURNS: 20 data points in JSON format as sepcified by the params
		session = rauth.OAuth1Session(
			consumer_key = keys['CONSUMER_KEY'],
			consumer_secret = keys['CONSUMER_SECRET'],
			access_token = keys['TOKEN'],
			access_token_secret = keys['TOKEN_SECRET'])

		params = {}
		params["term"] = "happy+hour"
		params["location"] = "Vancouver+BC+Canada"
		params["offset"] = offset

		request = session.get("http://api.yelp.com/v2/search", params=params)

		a_set = request.json()
		session.close()

		return a_set

class TranslatePostYelp(object):

	def post_all_to_database(self):
		"""
		Post to database using data from data.json file
		:return: String of status
		"""
		with open('data.json') as data_file:
			data = json.load(data_file)
		for restaurant in data['businesses']:
			formatted_data = self.format_data(restaurant)
			post = self.post_to_database(formatted_data)
			if not post:
				print "Could not post: "
				pprint(formatted_data)

	def format_data(self, restaurant):
		"""
		Format and parse data based on webapp's database.
		:param restaurant: data for restaurant
		:return: formatted data of restaurant
		"""
		name = restaurant['name']
		address_list = restaurant['location']['display_address']
		address = " ".join(address_list)
		if 'phone' in restaurant:
			phone_number = restaurant['phone']
		else:
			phone_number = ""
		rating = restaurant['rating']
		location_lat = restaurant['location']['coordinate']['latitude']
		location_long = restaurant['location']['coordinate']['longitude']
		image_url = restaurant['image_url']
		data = {'name': name, 'address': address, 'phone_number': phone_number,
				'rating': str(rating), 'location_lat': str(location_lat), 'location_long': str(location_long),
				'image_url': image_url}
		return data

	def post_to_database(self, data):
		"""
		post data to database
		:param data: data to post
		:return: boolean on whether or not post was successful
		"""
		post_url = webapp_url + api_post_url
		r = requests.post(post_url, data=data)
		if r.status_code == 201:
			return True
		else:
			return False

# def main():
# 	client = YelpClient()
# 	data = client.get_all_sets(keys, 200)
# 	print len(data[u'businesses'])
# 	with open('data.json', 'w') as outfile:
# 		json.dump(data, outfile, indent=2)
# 	post_yelp = TranslatePostYelp()
# 	post_yelp.post_all_to_database()
#
# if __name__=="__main__":
# 	main()
