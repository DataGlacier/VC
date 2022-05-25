#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 23 23:49:58 2022

@author: yuyangxie
"""

# Importing the libraries
import numpy as np
import pandas as pd
import pickle

dataset = pd.read_csv('wages.csv')

X = dataset.drop(columns = ['Wage', 'Race', 'Occup', 'Sect'])

y = dataset.iloc[:, 5:6]

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()

#Fitting model with trainig data
regressor.fit(X, y)

# Saving model to disk
pickle.dump(regressor, open('model_wages.pkl','wb'))

# Loading model to compare the results
model = pickle.load(open('model_wages.pkl','rb'))
print(model.predict([[16, 0, 0, 22, 0, 45, 1]]))
