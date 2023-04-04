from flask import Flask, request, render_template
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)
model = pickle.load(open('model/model.pkl', 'rb'))

def preprocess_input(input_data):
    # Preprocess the input data
    input_df = pd.DataFrame(input_data, index=[0])
    input_df = input_df.drop(columns=[col for col in input_df.columns if col not in 
                                       ['Price Of Sculpture', 'Artist Reputation',
                                        'Base Shipping Price', 'Weight', 'Width', 'Height']])
    return input_df
    
@app.route('/')
def home():
    return render_template('index.html')
    

@app.route('/predict', methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    try:
        # Get the input data from the HTML form
        input_data = request.form.to_dict()
        
        # Preprocess the input data
        input_df = preprocess_input(input_data)
        
        # Generate the prediction
        output = model.predict(input_df)[0]
        
        # Render the HTML template with the prediction result
        return render_template('index.html', prediction_text='The estimated cost of shipping is $ {:.2f}'.format(output))

    except Exception as e:
        print(e)
        return 'Error: {}'.format(e)


if __name__== '__main__':
    app.run(debug = True)
