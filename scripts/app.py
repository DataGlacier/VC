from flask import Flask, render_template, request#, redirect, url_for, flash, jsonify

app = Flask(__name__)


@app.route('/')
def home():
    return 'Hello World'
    


if __name__ == '__main__':
    app.run(host='localhost', port=8080, debug=True)
