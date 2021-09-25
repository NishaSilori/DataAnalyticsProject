import matplotlib
import pandas as pd
from matplotlib import pyplot as plt

from load_CSV_file import data
print(data)
print(data.columns)
print(len(data.columns))
print(len(data))
print(data.info())
print(data.describe())
print(data)
numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
numeric_df=data.select_dtypes(include=numerics)
print(len(numeric_df.columns))
missing_percentage=data.isnull().sum().sort_values(ascending=False)/len(data)
print(missing_percentage)
print(type(missing_percentage))
print(missing_percentage.plot(kind='bar'))
print(missing_percentage.plot.bar())
print(plt.show())
print(data['country_or_area'].unique())
print(data['country_or_area'].value_counts())
print(data['commodity'].unique())
print(data['commodity'].value_counts())
print(data['category'].unique())
print(data['category'].value_counts())
print(data['commodity'].unique()[:10])
data.drop('weight_kg',axis='columns',inplace=True)
print(data)
print(data[['quantity','commodity']])
print(data[['quantity','commodity']].isnull())
print(data[['quantity','commodity']].isnull().sum())
print(data.head())
data.quantity=data.groupby('category')['quantity'].apply(lambda x:x.fillna(x.mean()))
data.quantity.fillna(data.quantity.mean())
final_missing_percentage=data.isnull().sum()
print(final_missing_percentage.plot.bar())
print(plt.show())
print(data.iloc[1048571 :1048572 ,4:5])
dummies=pd.get_dummies(data.flow)
merge_data=pd.concat([data,dummies],axis='columns')
print(merge_data)



