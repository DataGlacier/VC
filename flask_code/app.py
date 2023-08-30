from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
#import pandas as pd

class UploadFileForm(FlaskForm):
    file = FileField("File")
    submit = SubmitField("Upload File")


app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'

@app.route("/")
@app.route('/home', methods=['GET',"POST"])
def home():
    form = UploadFileForm()
    return render_template('index.html', form=form)
app.run(host="0.0.0.0", port =80)

#Data
#df_bonus = pd.read_csv('C:\Users\js940\Downloads\DataSets-main\City.csv')
#df_bonus

#data = pd.read_csv('C:\Users\js940\Downloads\DataSets-main\Customer_ID.csv')
#data



#from flask import Flask, render_flask, request
#import flask

#app = Flask('__name__')

#@app.route('/')
#def index():
#    return render_flask("index.html")

#if __name__ == '__main__':
#    app.run(debug=True)
