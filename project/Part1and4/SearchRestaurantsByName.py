__author__ = 'chianti'

import pandas as pd

from SearchByNameFuncs import *
from InputCheck import *


data = pd.read_csv('yelp_restaurant_only_dataset.csv')


def main():

    if 1 == 1:

        '''
        The first while loop checks the validity of the input
        If the input is a string which contains only alphabetic characters besides whitespaces, read the input as
        get_partial_name, otherwise, raise errors
        '''
        while True:

            try:
                get_partial_name = raw_input('Type in a restaurant\'s partial or full name to get more information: ')
                break
            except InputNotStringError or RestNameContainNonAlphaError:
                print 'Sorry, can not recognize your input.'

        # Use NameSearch() to get a DataFrame with all the restaurants match get_partial_name
        test = NameSearch(data, str(get_partial_name))

        # Print partial columns in the test DataFrame
        # Note: the result still contains NaN values
        print GetUsefulInfo(test)

if __name__ == '__main__':
    main()

