#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 23 23:49:02 2022

@author: yuyangxie
"""

import numpy as np
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model_wages.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index_wages.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = np.round(prediction[0], 2)

    return render_template('index_wages.html', prediction_text='Wage should be $ {} k'.format(output))

if __name__ == "__main__":
    app.run(debug=True)