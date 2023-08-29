from flask import Flask, render_flask, request

app = Flask('__name__')

@app.route('/')
def index():
    return render_flask("index.html")

if __name__ == '__main__':
    app.run(debug=True)
