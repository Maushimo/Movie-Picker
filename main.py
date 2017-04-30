from flask import Flask, render_template, request
#libraries to handle JSON data
import urllib2
import json

app = Flask(__name__)

apiKey = '80416fb595924fbedeb1769fc60f0579'
#main TMDB api url
mainAPI = 'https://api.themoviedb.org/3'
keywordSearch = '/search/keyword?api_key=' + apiKey

#default page
@app.route('/')
def index():
	return render_template('index.html')

#page to display suggested movie
@app.route('/Search-movies', methods=['POST'])
def searchMovie():
	#grab keywords from html page
	keywords = request.form['keywords']
	keywordQuery = mainAPI + keywordSearch + '&query=' + keywords

	jsonObj = urllib2.urlopen(keywordQuery)
	data = json.load(jsonObj)

	#array for movieIDs pulled from TMDB
	movieIDs = []
	#iterate through the results
	for i in data['results']:
		#'push_back' all the ids found
		movieIDs.append(i['id'])

	#pull up the first ID in the list
	movie = movieIDs[0]
	return render_template('movie-search.html', movie=movie)