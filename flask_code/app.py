from flask import Flask, render_flask_code, request

app = Flask('__name__')

@app.route('/')
def index():
    return render_flask_code("index.html")

if __name__ == '__main__':
    app.run(debug=True)
