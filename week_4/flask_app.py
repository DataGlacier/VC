import numpy as np
from flask import Flask, request, render_template
import tensorflow as tf
import keras.utils as image
from keras.datasets import cifar10
from keras.applications.resnet import ResNet50, preprocess_input, decode_predictions


app = Flask(__name__)
model = ResNet50()

@app.route('/')
def start_fn():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def predict():
    imagefile= request.files['imagefile']
    image_path = "./images/" + imagefile.filename
    imagefile.save(image_path)

    image1 = image.load_img(image_path, target_size=(224, 224))
    image1 = image.img_to_array(image1)
    image1 = preprocess_input(image1)

    image1 = tf.expand_dims(image1, axis=0)

    preds = model.predict(image1)
    label = decode_predictions(preds)
    label = label[0][0]
    
    classification = '%s (%.2f%%)' % (label[1], label[2]*100)
    return render_template('index.html', prediction = classification)



if __name__ == '__main__':
    app.run(port=3000, debug=True)