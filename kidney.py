# -*- coding: utf-8 -*-
"""kidney.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rN8EugokHfIfaDZfGyoXYMJqHZ3DUvKH
"""

import pandas as pd #used for data manipulation

import numpy as np #used for numerical analysis

from collections import Counter as c # return counts of number of classess

import matplotlib.pyplot as plt #used for data visualization

import seaborn as sns #data visualization librory

import missingno as msno #finding missing values

from sklearn.metrics import accuracy_score, confusion_matrix#model performance

from sklearn.model_selection import train_test_split #splics data in randam train and test array

from sklearn.preprocessing import LabelEncoder #encoding the levels of categotical features

from sklearn.linear_model import LogisticRegression #classification ML algorithm

import pickle #python object hierarchy is converted into a byte stream,

data = pd.read_csv(r"/content/kidney_disease.csv") #loading the csv data



data.head() #return you the first 5 rows values

data.columns #return all the column names

data.columns# rename column names to make it more user-friendly

data.shape
data.drop('id', axis = 1, inplace = True)

data.columns = ['age', 'blood_pressure', 'specific_gravity', 'albumin', 'sugar', 'red_blood_cells', 'pus_cell',
              'pus_cell_clumps', 'bacteria', 'blood_glucose_random', 'blood_urea', 'serum_creatinine', 'sodium',
              'potassium', 'haemoglobin', 'packed_cell_volume', 'white_blood_cell_count', 'red_blood_cell_count',
              'hypertension', 'diabetes_mellitus', 'coronary_artery_disease', 'appetite', 'peda_edema',
              'aanemia', 'class']
data.columns

data.info()

#extracting numaric and categorical data 

num_cols = [col for col in data.columns if data[col].dtype != 'object']
cat_cols = [col for col in data.columns if data[col].dtype == 'object']

num_cols

#####check unique values in the categorical data 

for col in cat_cols:
    print(f"{col} has {data[col].unique()} values\n")

#####to handel the skewness in the data 
def handel_outlier(col):
    data[col] =np.log1p(data[col])

handel_outlier('blood_urea')
handel_outlier('sodium')
handel_outlier('potassium')
handel_outlier('serum_creatinine')
handel_outlier('sugar')

##that explins why soe data still skeness although we to process on it  , becaus it stil has null data 
data.isna().sum()

#filling null values, we will use two methods, random sampling for higher null values and 
# mean/mode sampling for lower null values
def random_value_imputation(feature):
    random_sample = data[feature].dropna().sample(data[feature].isna().sum())
    random_sample.index = data[data[feature].isnull()].index
    data.loc[data[feature].isnull(),feature] =random_sample
    
def impute_mode(feature):
    mode = data[feature].mode()[0]
    data[feature] =data[feature].fillna(mode)

###filling num columns null values uysing rando sampling method

for col in num_cols:
    random_value_imputation(col)

data[num_cols].isnull().sum()

# heatmap of data

plt.figure(figsize = (15, 8))

sns.heatmap(data.corr(), annot = True, linewidths = 2, linecolor = 'lightgrey')
plt.show()

# looking at categorical columns

plt.figure(figsize = (20, 15))
plotnumber = 1

for column in cat_cols:
    if plotnumber <= 11:
        ax = plt.subplot(3, 4, plotnumber)
        sns.countplot(data[column], palette = 'rocket')
        plt.xlabel(column)
        
    plotnumber += 1

plt.tight_layout()
plt.show()

data[cat_cols].isnull().sum()

# checking for null values

data.isna().sum().sort_values(ascending = False)

# checking numerical features distribution

plt.figure(figsize = (20, 15))
plotnumber = 1

for column in num_cols:
    if plotnumber <= 14:
        ax = plt.subplot(3, 5, plotnumber)
        sns.distplot(data[column])
        plt.xlabel(column)
        
    plotnumber += 1

plt.tight_layout()
plt.show()

for col in cat_cols:
    print(f"{col} has {data[col].unique()} values\n")

data.describe()

!pip install nbconvert

! jupyter nbconvert --to html kidney.ipynb

!pip install flask-ngrok

