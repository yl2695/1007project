from Part1and4.Part1and4Exceptions import *
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D

def NameSearch(df, partial_name):
    """
    NameSearch function searches for a restaurant in the df given a partial_name
    :param df: a DataFrame
    :param partial_name: a string type
    :return: the selected rows of df with partial_name in the 'name' column, ignoring upper or lower case
    """
    if partial_name == '$':
        raise NameSearchNoResultError('Sorry, no result. Try another name ?')
    if partial_name == '^':
        raise NameSearchNoResultError('Sorry, no result. Try another name ?')
    search_result = df[df['name'].str.contains(partial_name, case=False)]
    search_result = search_result[['name', 'city', 'state', 'stars', 'latitude', 'longitude']]

    if search_result.empty:
    # if search_result is empty, which means that there is no match for partial_name, an exception raises
        raise NameSearchNoResultError('Sorry, no result. Try another name ?')

    else:
        return search_result


def plot3dDistribution(df):
    latitudeRange = df['latitude']
    longitudeRange = df['longitude']
    starRange = df['stars']
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(latitudeRange, longitudeRange, starRange)
    ax.set_xlabel('latitude')
    ax.set_ylabel('longitude')
    ax.set_zlabel('stars')
    plt.show()



def GetUsefulInfo(df):
    """
    GetUsefulInfo is used to get four features from df
    :param df: a DataFrame
    :return:the selected columns of the df
    """

    return df[['name', 'city', 'state', 'stars']]




