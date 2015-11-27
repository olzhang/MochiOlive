import unittest
from django.test import TestCase
from happyhour.yelp_client import TranslatePostYelp
from happyhour.models import Restaurant

import json

def test_parser_empty():
    with open("happyhour/sample_empty.json") as data_file:
        empty_data = json.load(data_file)
    post_yelp = TranslatePostYelp()
    for restaurant in empty_data:
        formatted_data = post_yelp.format_data(restaurant)

def test_parser_check_data_helper(data):
    post_yelp = TranslatePostYelp()
    for restaurant in data:
        formatted_data = post_yelp.format_data(restaurant)
        assert formatted_data['name']
        assert formatted_data['address']
        assert formatted_data['phone_number']
        assert formatted_data['rating']
        assert formatted_data['location_lat']
        assert formatted_data['location_long']
        assert formatted_data['image_url']

class ParserTestCase(unittest.TestCase):
    def setUp(self):
        self.root = "happyhour/"
        with open(self.root + "sample.json") as data_file:
            self.good_data = json.load(data_file)
        with open(self.root + "sample_missing_param.json") as data_file:
            self.incomplete_data = json.load(data_file)
        with open(self.root + "sample_bad.json") as data_file:
            self.bad_data = json.load(data_file)

    # test with good and complete data with no missing attributes
    def test_parser_complete_data(self):
        test_parser_check_data_helper(self.good_data)

    # test with bad data - all attributes are there, but data is bad
    # shouldn't raise exceptions, since parser's job is only to parse, and not look at data
    def test_parser_bad_data(self):
        test_parser_check_data_helper(self.bad_data)

    # test with data that is missing attributes
    # should raise exception since json keys don't exist.
    def test_parser_incomplete_data(self):
        with self.assertRaises(Exception):
            test_parser_check_data_helper(self.incomplete_data)

    # test with empty data file
    # should raise exception since there is no json data. 
    def test_parser_empty_data(self):
        with self.assertRaises(ValueError):
            test_parser_empty()
