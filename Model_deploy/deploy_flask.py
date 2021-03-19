import numpy as np
from flask import Flask, request, render_template
import pickle


app = Flask(__name__)
model = pickle.load(open('pickle_model', 'rb'))


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction.model.predict(final_features)
    
    output = round(prediciont[0], 2)
    
    return render_template('index.html', prediction_text='CO2 emission for this size of engine should be {}'. format(output))


if __name__ == "__main__":
    app.run(port=5000, debug=True)
    