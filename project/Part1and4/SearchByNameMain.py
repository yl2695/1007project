__author__ = 'chianti'

from SearchByNameFuncs import *
import pandas as pd

data = pd.read_csv('yelp_restaurant_only_dataset.csv')

def main():

    if 1 == 1:

        get_partial_name = raw_input('Type in a restaurant\'s partial or full name to get more information: ')

        test = NameSearch(data, get_partial_name)
        # Use NameSearch() to get a DataFrame with all the restaurants match get_partial_name

        print GetUsefulInfo(test)
        # Print partial columns in the test DataFrame
        # Note: the result still contains NaN values

if __name__ == '__main__' and True:
    main()