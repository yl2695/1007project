import unittest
from pandas import DataFrame
from exceptionClass import InputError
from topRestaurantsInStateSelect import *
from topRestaurantInStateAndPriceSelect import *


class TestPart2(unittest.TestCase):
    '''
    Test the second part of the application.
    '''
	
    def setUp(self):
        '''
        set up testing data for the test.
        '''
        self.state1 = 'AZ'
        self.state2 = 'DS'
        self.num_top1 = 3
        self.num_top2 = -3
		
    def testtopRestaurantsInState(self):
        '''
        test topRestaurantsInState function
        '''
		
        # state:'AZ' and num_top = 3 should be a correct user input and thus it is expected to return a DataFrame.
        self.assertIsInstance(topRestaurantsInState(self.state1, self.num_top1), DataFrame)
		
        # state:'DS' or num_top = -3 are not right user input, thus it is expected to raise an exception.
        self.assertRaises(InputError, topRestaurantsInState, self.state1, self.num_top2)
        self.assertRaises(InputError, topRestaurantsInState, self.state2 ,self.num_top1)


class TestPart3(unittest.TestCase):
    '''
	Test part3 of this application.
	'''

    def setUp(self):
        '''
        set up testing data for the test
        '''

        self.state1 = 'WI'
        self.state2 = 'ds'
        self.price1 = 3
        self.price2 = 9
        self.num_top1 = 10
        self.num_top2 = -10
	
    def testrestaurantInStateandPrice(self):
        '''
        test restaurantInStateandPrice function.
        '''
		
        # state:'WI', price=3, num_top=10 should be correct user input and thus it is expected to return a DataFrame.
        self.assertIsInstance(restaurantInStateandPrice(self.state1,self.price1, self.num_top1), DataFrame)
		
        # None of state:'ds', price=9, num_top=-10 are correct user input and thus it is expected to raise an exception.
        self.assertRaises(InputError, restaurantInStateandPrice, self.state2, self.price1, self.num_top1)
        self.assertRaises(InputError, restaurantInStateandPrice, self.state1, self.price2, self.num_top1)
        self.assertRaises(InputError, restaurantInStateandPrice, self.state1, self.price1, self.num_top2)
	
	
if __name__ == '__main__':
    unittest.main()