from flask import Flask, request, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/sales', methods=['Post'])
def sales():
    Person = request.form.get('who')
    Day = request.form.get('day')
    return render_template('index.html', sales_week = "{}'s Sales for {} are: {}".format(Person, Day, model.loc[Person, Day]))


app.run(port=5000)
