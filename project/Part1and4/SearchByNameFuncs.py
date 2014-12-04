__author__ = 'chianti'

from SearchFuncsExceptions import *


def NameSearch(df, partial_name):
    # df is a DataFrame
    # partial_name is a string type
    # search for a restaurant in the df given a partial_name
    # return the selected rows of df with partial_name in the 'name' column
    # ignore upper or lower case
    search_result = df[df['name'].str.contains(partial_name, case=False)]
    search_result = search_result[['name', 'city', 'state', 'stars']]
    if search_result.empty:
        # if search_result is empty, which means that there is no match for partial_name, an exception raises
        raise NameSearchNoResultError('Sorry, no result. Try another name ?')

    else:
        return search_result


def GetUsefulInfo(df):
    # return only several columns of the df
    return df[['name', 'city', 'state', 'stars']]
