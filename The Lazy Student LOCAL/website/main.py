from flask import Flask, url_for
from markupsafe import escape
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
    