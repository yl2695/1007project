import pandas as pd


business_data = pd.read_csv('yelp_restaurant_only_dataset.csv')
checkin_data = pd.read_csv('yelp_academic_dataset_checkin.csv')

checkin_data = checkin_data.set_index('business_id')
checkin_data = checkin_data.fillna(0)
checkin_data = checkin_data.drop('type', 1)

check_Sunday = checkin_data[['checkin_info_{}-0'.format(str(x)) for x in range(24)]]

check_Monday = checkin_data[['checkin_info_{}-1'.format(str(x)) for x in range(24)]]

check_Tuesday = checkin_data[['checkin_info_{}-2'.format(str(x)) for x in range(24)]]

check_Wednesday = checkin_data[['checkin_info_{}-3'.format(str(x)) for x in range(24)]]

check_Thursday = checkin_data[['checkin_info_{}-4'.format(str(x)) for x in range(24)]]

check_Friday = checkin_data[['checkin_info_{}-5'.format(str(x)) for x in range(24)]]

check_Saturday = checkin_data[['checkin_info_{}-6'.format(str(x)) for x in range(24)]]