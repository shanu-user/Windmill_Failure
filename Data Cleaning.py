# Importing and loading libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Loading the dataset

df = pd.read_csv('Data Set/Wind_turbine.csv')

df

print(df.to_string())


# Descriptive Statistics
df.shape

df.describe()

df.info()


## Checking for datatypes
df.dtypes


## First moment business decision
for column in df.select_dtypes(include="number").columns:
    print(f'Mean of {column}: {df[column].mean()}')
    print(f'Median of {column}: {df[column].median()}')
    print(f'Mode of {column}: {df[column].mode()[0]}')


## Second moment business decision

for column in df.select_dtypes(include="number").columns:
    print(f'Variance of {column}: {df[column].var()}')
    print(f'Standard Deviation of {column}: {df[column].std()}')
    print(f'Range of {column}: {df[column].max() - df[column].min()}')


## Third moment business decision

for column in df.select_dtypes(include="number").columns:
    print(f'Skewness of {column}: {df[column].skew()}')

## Fourth moment business decision

for column in df.select_dtypes(include="number").columns:
    print(f'Kurtosis of {column}: {df[column].kurt()}')





# Handling missing values
df.isnull().sum()




## Checking for duplicates

df.duplicated().sum()
