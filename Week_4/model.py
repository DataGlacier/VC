import pandas as pd
import numpy as np
import pickle

dataset = pd.read_csv('sales.csv', index_col = 'Unnamed: 0')

dataset.Thu.fillna(0, inplace = True)

dataset.Thu = dataset.Thu.astype(int)

dataset['Total'] = dataset.sum(axis = 1)

pickle.dump(dataset, open('model.pkl', 'wb'))
