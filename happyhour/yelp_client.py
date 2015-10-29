import rauth 
import pprint
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

# def main():
# 	client = YelpClient()
# 	data = client.get_all_sets(keys, 200)
# 	print len(data[u'businesses'])
# 	with open('data.json', 'w') as outfile:
# 		json.dump(data, outfile, indent=2)

# if __name__=="__main__":
# 	main()
