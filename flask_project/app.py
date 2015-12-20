from flask import Flask, render_template, jsonify
from jinja2 import Template

app = Flask(__name__, static_folder='static')

@app.route('/')
def home():
	'''
	home() will show the homepage of my website
	'''
	return render_template('index.html')	

if __name__ == '__main__':
    app.run()
