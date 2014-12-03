__author__ = 'chianti'


class NameSearchNoResultError(Exception):
    '''When the user is using the function NameSearch(df, partial_name), while there is no partial_name in the 'name' feature in the df DataFrame, NameSearchNoResultError raises. 
    '''
    pass


class StateSearchNoResultError(Exception):
    '''
    When the user is using the function StateSearch(df, state_name), while state_name is not a state abbreviation
    from {'ON', 'ELN', 'EDH', 'MLN', 'WI', 'NY', 'KHL', 'AZ', 'CA', 'NV'}, StateSearchNoResultError raises

    '''
    pass