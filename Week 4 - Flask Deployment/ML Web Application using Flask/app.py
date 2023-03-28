from flask import Flask, request, render_template
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)
model = pickle.load(open('model/model.pkl', 'rb'))

def manipulation(df):
    df['State']= df['Customer Location'].str.split(" ").str[-2]


@app.route('/')
def home():
    return render_template('html/index.html')

@app.route('/predict', methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    # Get the input data from the HTML form
    input_data = request.form.to_dict()
    
    # Preprocess the input data
    input_df = pd.DataFrame(input_data, index=[0])
    #input_df = manipulation(input_df)
    input_df = input_df.drop(columns=[col for col in input_df.columns if col not in 
                                       ['Price Of Sculpture', 'State', 'Artist Reputation',
                                        'Base Shipping Price', 'Weight']])
    
    # Generate the prediction
    prediction = model.predict(input_df)[0]
    
    # Render the HTML template with the prediction result
    return render_template('html/index.html', prediction_text='Shipping Cost Estimate is $ {}'.format(prediction))

if __name__== '__main__':
    app.run(debug = True)
