import pandas as pd


business_data = pd.read_csv('yelp_restaurant_only_dataset.csv')
checkin_data = pd.read_csv('yelp_training_set_checkin.csv')

checkin_data = checkin_data.set_index('business_id')
checkin_data = checkin_data.fillna(0)
checkin_data = checkin_data.drop('type', 1)

check_Sunday = checkin_data[['checkin_info_0-0', 'checkin_info_1-0', 'checkin_info_2-0', 'checkin_info_3-0', 'checkin_info_4-0', 'checkin_info_5-0', 'checkin_info_6-0', 'checkin_info_7-0', 'checkin_info_8-0', 'checkin_info_9-0']]

check_Monday = checkin_data[['checkin_info_0-1', 'checkin_info_1-1', 'checkin_info_2-1', 'checkin_info_3-1', 'checkin_info_4-1', 'checkin_info_5-1', 'checkin_info_6-1', 'checkin_info_7-1', 'checkin_info_8-1', 'checkin_info_9-1']]

check_Tuesday = checkin_data[['checkin_info_0-2', 'checkin_info_1-2', 'checkin_info_2-2', 'checkin_info_3-2', 'checkin_info_4-2', 'checkin_info_5-2', 'checkin_info_6-2', 'checkin_info_7-2', 'checkin_info_8-2', 'checkin_info_9-2']]

check_Wednesday = checkin_data[['checkin_info_0-3', 'checkin_info_1-3', 'checkin_info_2-3', 'checkin_info_3-3', 'checkin_info_4-3', 'checkin_info_5-3', 'checkin_info_6-3', 'checkin_info_7-3', 'checkin_info_8-3', 'checkin_info_9-3']]

check_Thursday = checkin_data[['checkin_info_0-4', 'checkin_info_1-4', 'checkin_info_2-4', 'checkin_info_3-4', 'checkin_info_4-4', 'checkin_info_5-4', 'checkin_info_6-4', 'checkin_info_7-4', 'checkin_info_8-4', 'checkin_info_9-4']]

check_Friday = checkin_data[['checkin_info_0-5', 'checkin_info_1-5', 'checkin_info_2-5', 'checkin_info_3-5', 'checkin_info_4-5', 'checkin_info_5-5', 'checkin_info_6-5', 'checkin_info_7-5', 'checkin_info_8-5', 'checkin_info_9-5']]

check_Saturday = checkin_data[['checkin_info_0-6', 'checkin_info_1-6', 'checkin_info_2-6', 'checkin_info_3-6', 'checkin_info_4-6', 'checkin_info_5-6', 'checkin_info_6-6', 'checkin_info_7-6', 'checkin_info_8-6', 'checkin_info_9-6']]

print checkin_data[checkin_data.index == 'qarobAbxGSHI7ygf1f7a_Q']

#print check_Saturday
