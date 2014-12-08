__author__ = 'chianti'

from RestAndStateNameCheckFuncs import *
from Part1and4Exceptions import *


class RestaurantName():
    """
    RestaurantName class is used to test whether the input, which is supposed to indicate a partial or full name of a
    restaurant given by the user, is a valid one.
    I.e: this class helps to check whether the input is a string and whether it contains non alphabetic characters
    besides whitespaces.
    """

    def __init__(self, input_contents):

        self.name = input_contents

        # First, check whether self.name is a string type
        if IsValidString(self.name):

            # Remove spaces from self.name
            self.no_space_name = self.name.replace(' ', '')

            # Check whether the input contains non alphabetic characters, after removing the white spaces in it
            if str.isalpha(self.no_space_name):
                pass
            else:
                raise RestNameContainNonAlphaError('There are non alphabetic characters that I can not recognize!')

        else:

            raise InputNotStringError('Not String! The input is supposed to be a string type!')

    def __repr__(self):

        return 'RestaurantName(%s)' % self.name.strip()  # Note: removed leading and ending spaces here

    def __str__(self):

        return self.name.strip()   # Note: removed leading and ending spaces here



class StateName():
    """
    StateName class is used to test whether the input, which is supposed to indicate a state, is a valid one.
    I.e: this class helps to check whether the input is an element from:
                {'ON', 'ELN', 'EDH', 'MLN', 'WI', 'NY', 'KHL', 'AZ', 'CA', 'NV'}
    """

    def __init__(self, input_state):

        self.state_name = input_state

        # First, check whether self.name is a string type
        if IsValidString(self.state_name):
            pass
        else:
            raise StateNotStringError('Not String! The input is supposed to be a string type!')

        # Remove spaces from self.name and make it all upper letters
        self.no_space_state_name = self.state_name.replace(' ', '')
        self.upper_state_name = self.no_space_state_name.upper()

        # Check whether the input contains non alphabetic characters, after removing the white spaces in it
        if str.isalpha(self.upper_state_name):
            pass
        else:
            raise StateNameContainNonAlphaError('There exist non alphabetic characters that I can not recognize!')

        # Check whether the input is an element from:
        #                       {'ON', 'ELN', 'EDH', 'MLN', 'WI', 'NY', 'KHL', 'AZ', 'CA', 'NV'}
        if IsValidState(self.upper_state_name):
            pass
        else:
            raise InvalidStateNameError('Sorry, cannot recognize the state name! ')

    def __repr__(self):
        return 'StateName(%s)' % self.upper_state_name.strip()  # Note: removed leading and ending spaces here

    def __str__(self):
        return self.upper_state_name.strip().upper()   # Note: removed leading and ending spaces here

