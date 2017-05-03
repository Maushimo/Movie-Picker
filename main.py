from flask import Flask, render_template, request
#libraries to handle JSON data
import urllib2
import json

app = Flask(__name__)

apiKey = '?api_key=80416fb595924fbedeb1769fc60f0579'
#main TMDB api url
mainAPI = 'https://api.themoviedb.org/3'

#default page
@app.route('/')
def index():
	return render_template('index.html')

#page to display suggested movie
@app.route('/Search-movies', methods=['POST'])
def searchMovie():
	keywordSearch = '/search/multi' + apiKey
	#grab keywords from html page
	keywords = request.form['keywords']
	#replace the spaces with '%20' to prevent internal server errors
	replacedKeywords = keywords.replace(' ', '%20')
	keywordQuery = mainAPI + keywordSearch + '&include_adult=false' + '&query=' + replacedKeywords

	#print the URI for debugging
	print(keywordQuery)

	#query the website and store the json file into this object
	keywordJsonObj = urllib2.urlopen(keywordQuery)
	data = json.load(keywordJsonObj)

	#array for movieIDs pulled from TMDB
	movieIDs = []
	#iterate through the results
	for i in data['results']:
		#'push_back' all the ids found
		movieIDs.append(i['id'])

	#pull up the first ID in the list
	movieIDsIndex = 0
	movie = movieIDs[movieIDsIndex]
	#grabs movie details
	getMovieDetailsQuery = mainAPI + '/movie/' + str(movie) + apiKey

	#print the URI for debugging
	print(getMovieDetailsQuery)

	#same process as keyword...
	movieDetailsJsonObj = urllib2.urlopen(getMovieDetailsQuery)
	movieDetails = json.load(movieDetailsJsonObj)

	#grab the movie title
	movieTitle = movieDetails['title']

	posterPath = movieDetails['poster_path']
	poster = 'https://image.tmdb.org/t/p/w1280' + posterPath

	return render_template('movie-search.html', movieTitle=movieTitle, poster=poster)