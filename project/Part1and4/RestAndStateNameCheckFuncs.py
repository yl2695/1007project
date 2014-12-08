__author__ = 'chianti'


def IsValidString(content):
    """
    IsValidString(content) checks whether content is a string type
    It is used in two classes: RestaurantName and StateName, both located under Package1and4/InputCheckClasses.py

    :param content: the input given by the user
    :return:True if the type of content is string
            False if the type of content is not string
    """

    if type(content) == str:
        return True
    else:
        return False


def IsValidState(content):
    """
    IsValidState(content) checks whether content is an element from:
                                 {'ON', 'ELN', 'EDH', 'MLN', 'WI', 'NY', 'KHL', 'AZ', 'CA', 'NV'}
    It is used StateName class, located under Package1and4/InputCheckClasses.py

    :param content: the input given by the user, which is supposed to indicate a state name
    :return:True if content is an element from:
                                 {'ON', 'ELN', 'EDH', 'MLN', 'WI', 'NY', 'KHL', 'AZ', 'CA', 'NV'}
            False if content is not an element from:
                                 {'ON', 'ELN', 'EDH', 'MLN', 'WI', 'NY', 'KHL', 'AZ', 'CA', 'NV'}
    """

    valid_state = ['ON', 'ELN', 'EDH', 'MLN', 'WI', 'NY', 'KHL', 'AZ', 'CA', 'NV']
    if content in valid_state:
        return True
    else:
        return False