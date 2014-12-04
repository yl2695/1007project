__author__ = 'chianti'

import unittest
from InputCheck import *
from Part1and4Exceptions import *
from PlotDistributionFuncs import PlotPieChartForOneState

'''
class RestaurantNameTests(unittest.TestCase):

    def setUp(self):

        self.non_string_name = 123
        self.valid_name = 'Italian rest '
        self.non_alpha_name = 'valid ** n'

    def test_non_string_name(self):

        self.assertRaises(InputNotStringError, RestaurantName, self.non_string_name)

    def test_valid_name(self):

        self.assertEqual(RestaurantName(self.valid_name).__str__(), 'Italian rest')

    def test_non_alpha_name(self):

        self.assertRaises(RestNameContainNonAlphaError, RestaurantName, self.non_alpha_name)
'''


class StateNameTests(unittest.TestCase):

    def test_non_string_state(self):

        self.assertRaises(StateNotStringError, StateName, 222)

    def test_non_alpha_state(self):

        self.assertRaises(StateNameContainNonAlphaError, StateName, 'wi*')

    def test_invalid_state(self):

        self.assertRaises(InvalidStateNameError, StateName, 'WW')

    def test_valid_state(self):

        self.assertEqual(StateName('ny').__str__(), 'NY')


class PlotPieChartForOneStateTest(unittest.TestCase):

    def test_invalid_state_pie_chart(self):

        self.assertRaises(NoValidPieChartForOneStateError, PlotPieChartForOneState, 'CA')

if __name__ == '__main__':

    unittest.main()


