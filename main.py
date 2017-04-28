from flask import Flask, render_template, request

app = Flask(__name__)

#default page
@app.route('/')
def index():
	return render_template('index.html')

#page to display suggested movie
@app.route('/Search-movies', methods=['POST'])
def searchMovie():
	return render_template('movie-search.html')
