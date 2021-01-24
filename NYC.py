import pandas as pd
import numpy as np
import sklearn

data = pd.read_csv("AB_NYC_2019.csv")
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)

data.drop(['id', 'host_id', 'host_name', 'last_review', 'reviews_per_month'], 1, inplace = True)
data['name'].fillna('Name not provided', inplace = True)

spec_data = data.loc[data['neighbourhood_group'] == 'Brooklyn']
spec_data = spec_data[spec_data.price != 0]

spec_data = spec_data.loc[spec_data['room_type'] == 'Private room']

spec_data = spec_data[spec_data.price>= 60 ]
final_data = spec_data.sort_values(by=['price'])

print(final_data)