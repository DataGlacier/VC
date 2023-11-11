# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 14:32:59 2023

@author: cdbry
"""

import numpy as np
import pandas as pd
from flask import Flask, request, render_template
from sklearn.ensemble import RandomForestRegressor

train_data = pd.read_csv(r"C:\Users\cdbry\Desktop\Data Glacier Internship\Repositories\Data-Glacier-Internship-Fall-2023\Week 4\Deployment_Flask\data/train.csv")
test_data = pd.read_csv(r"C:\Users\cdbry\Desktop\Data Glacier Internship\Repositories\Data-Glacier-Internship-Fall-2023\Week 4\Deployment_Flask\data/test.csv")


app = Flask(__name__)


y = train_data["Survived"]
features = ["SibSp", "Parch"]
X = pd.get_dummies(train_data[features].dropna(how ='any'))




model = RandomForestRegressor(n_estimators=100, max_depth=5, random_state=1)
model.fit(X, y)


@app.route('/')

def home():
    return render_template("template.html")


@app.route('/predict', methods = ['POST'])

def predict():
    """
    For rending results on HTML GUI
    """
    
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    
    return render_template('template.html', prediction_text = f"Probability they survived: {prediction[0]}")
    
                           
if __name__ == "__main__":
    app.run(port = 5000, debug = True)