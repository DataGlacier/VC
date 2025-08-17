import joblib
import numpy as np

model = joblib.load('model.joblib')

def predict(event, context):
    input_data = np.array(event['body']).reshape(1, -1)
    prediction = model.predict(input_data)
    return {'prediction': int(prediction[0])}