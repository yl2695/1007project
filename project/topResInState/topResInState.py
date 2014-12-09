import pandas as pd
import matplotlib.pyplot as plt
from exceptionClass import InputError


f = pd.read_csv('yelp_restaurant_only_dataset.csv')


def topRestaurantsInState(state,num_top):
	'''
	This function will select out top restaurants in given state and given number.
	'''
	
	if state not in ['WI', 'AZ', 'NV', 'CA', 'ON', 'EDH', 'ELN', 'MLN', 'NY', 'KHL'] :
		raise InputError('Wrong state. ')
		
	if not(num_top > 0):
		raise InputError('Wrong number of TOP. ')
		
	#Select out all restaurants in given state.
	select_restaurants = f[f['state'] == state]
	
	#Sort restaurants according to stars; if several restaurants have the same stars, compare their review counts;
	#if still the same, sort it in descending alphabetical order.
	sorted_restaurants = select_restaurants.sort(['stars','review_count', 'name'], ascending=False)
	
	return sorted_restaurants[:num_top]


def restaurantStarsPlot(restaurants):
	'''
	This function will display a graph showing how many stars and review counts these restaurants have.
	'''

	# Parameter restaurants should be a DataFrame passed from function topRestaurantsInState.
	topRestaurants = restaurants.set_index('name')
	
	#Display 'stars' and 'review_count' in two sub_plots. 
	
	fig = plt.figure()
	
	ax1 = fig.add_subplot(1,2,1)
	topRestaurants['stars'].plot(kind = 'bar')
	
	ax2 = fig.add_subplot(1,2,2)
	topRestaurants['review_count'].plot(kind = 'bar')
	
	plt.show()
	
def restaurantsMoreInformation(restaurants):
	'''
	Give all information we have on given restaurants.
	'''

	# Parameter restaurants should be a DataFrame passed from function topRestaurantsInState.
	
	return restaurants.set_index('name')[['stars', 'attributes_Price Range','city']]