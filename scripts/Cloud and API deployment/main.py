#using flask to make an api for prediction insurance charges
import pandas as pd
from flask import Flask, request,render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))
def categoricalValueToInt(word):
    word_dict = {'female': 1, 'male': 2, 'yes':1,'no':2,'southwest':1,'southeast':2,'northwest':3,'northeast':4}
    if word in word_dict:
        return word_dict[word]
    else:
        return 0  # Handle unknown/invalid values with a default encoding
    

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(request.form['age']),
                    categoricalValueToInt(request.form['sex']),
                    float(request.form['bmi']),
                    int(request.form['children']),
                    categoricalValueToInt(request.form['smoker']),
                    categoricalValueToInt(request.form['region'])]
    
    # Create a DataFrame from int_features
    test_df = pd.DataFrame([int_features], columns=['age','sex','bmi','children','smoker','region'])

    # final_features = [np.array(encoded_features)]
    prediction = model.predict(test_df)

    output = round(prediction[0], 2)

    return render_template('index.html', prediction_text='Insurance charge should be $ {}'.format(output))

if __name__ == "__main__":
    app.run(port = 5000,debug=True)