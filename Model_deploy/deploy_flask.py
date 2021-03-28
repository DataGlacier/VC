import numpy as np
from flask import Flask, request, render_template, jsonify, make_response
import pickle


app = Flask(__name__)
with open('pickle_model.pkl', 'rb') as f:
    model = pickle.load(f)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    
    prediction = round(prediction[0][0], 2)
    
    return render_template('index.html', prediction_text='CO2 emission for this size of engine should be {} G/KM'
                           .format(prediction))

@app.route('/api')
@app.route('/api/')
@app.route('/api/<l>')
@app.route('/api/<l>/')
def api_l(l=None):
    if not l:
        message = jsonify(message='Size of engine (l) not provided')
        return make_response(message, 400)
    else:
        l = float(l)
        prediction = model.predict(np.array([[l]]))
        prediction = round(prediction[0][0], 2)
        return jsonify(
            CO2_emission=prediction,
            engine_size=l)


if __name__ == "__main__":
    app.run(port=5000, debug=True)
