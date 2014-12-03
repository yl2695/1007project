from question3 import restaurantInStateandPrice
from exceptionClass import InputError
import pandas as pd
import sys

def main():

	
	while True:
		
		print "We have records in following states: WI, AZ, NV, CA, ON, EDH, ELN, MLN, NY, KHL."
		print "Price ranges from 1 to 4(inclusive). "
		
		# Get input from user for selected state and expected maximum cost. 
		# Input doesn't follow the instruction will raise exception.
		try:
			state = raw_input('Which state do you want to look into? \n')
			price = int(raw_input('From 1 to 4, what is your maximum expected price?  \n'))
			num_top = int(raw_input('How many restaurants meeting the requirements do you want to see? \n'))
			
			print "These are TOP 10 restaurants in {} with price below and containing {}. ".format(state, '$'*price)
			restaurants = restaurantInStateandPrice(state,price,num_top)
			print restaurants
			
		except (InputError, ValueError):
			print 'Invalid input, please follow the instruction. '
			
		except (KeyboardInterrupt,IOError):
			print 'Thanks for using. '
			sys.exit()
	
	
if __name__ == '__main__':
	main()