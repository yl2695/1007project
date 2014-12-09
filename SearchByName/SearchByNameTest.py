__author__ = 'chianti'

from SearchByName.SearchByNameFuncs import *
import pandas as pd
import unittest


data = pd.read_csv('yelp_restaurant_only_dataset.csv')
# Load the data set


class NameSearchNoResultErrorTest(unittest.TestCase):
    """
    This class is used to test whether NameSearch function, located under SearhByNameFuncs.py, can raise the correct
    exceptions for invalid input
    """

    def test_name_search_special_character1(self):

        self.assertRaises(NameSearchNoResultError, NameSearch(data, '$'))

    def test_name_search_special_character2(self):

        self.assertRaises(NameSearchNoResultError, NameSearch(data, '^'))

if __name__ == '__main__':

    unittest.main()
