from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
	return "<h1>Hello</h1>"
	
if __name__ == "__main__":
	app.run()