import rauth
import requests
from pprint import pprint
import json

# Comment out main file at the bottom to test if it works
# in the terminal run 'python yelp_client'
# should write out json into data.json 

keys = {
	'CONSUMER_KEY': '',                  # access tokens removed for security purposes
	'CONSUMER_SECRET': '',
	'TOKEN': '',
	'TOKEN_SECRET': '',
}

webapp_url = ""                          # web app url removed
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
		return data[u'businesses']


	def _get_single_data_set(self, keys, offset):
		# PRE: keys: dictionary of yelp keys; 
		#      offset: the next n set of data points we want (each set in 20 data points big)
		# POST: nothing 
		# RETURNS: 20 data points in JSON format as sepcified by the params
		session = rauth.OAuth1Session(consumer_key = keys['CONSUMER_KEY'],consumer_secret = keys['CONSUMER_SECRET'],access_token = keys['TOKEN'],access_token_secret = keys['TOKEN_SECRET'])

		params = {}
		params["term"] = "happy+hour"
		params["location"] = "Vancouver+BC+Canada"
		params["offset"] = offset

		request = session.get("https://api.yelp.com/v2/search", params=params)

		a_set = request.json()
		session.close()

		return a_set

class TranslatePostYelp(object):

	def post_all_to_database(self, data):
		"""
		Post to database using data from data.json file
		:return: String of status
		"""
		for restaurant in data:
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
		name = self.check_key('name', restaurant)
		address_list = self.check_key('display_address', restaurant['location'])
		if address_list is not None:
			address = " ".join(address_list)
		else:
			address = None
		phone_number = self.check_key('phone', restaurant)
		rating = self.check_key('rating', restaurant)
		location_lat = self.check_key('latitude', restaurant['location']['coordinate'])
		location_long = self.check_key('longitude', restaurant['location']['coordinate'])
		image_url = self.check_key('image_url', restaurant)
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

	def check_key(self, name, restaurant):
		if name in restaurant:
			return restaurant[name]
		else:
			return None

def main():
	client = YelpClient()
	data = client.get_all_sets(keys, 200)
	print len(data)
	post_yelp = TranslatePostYelp()
	post_yelp.post_all_to_database(data)

if __name__=="__main__":
	main()
