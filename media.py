import webbrowser

class Movie():
	def __init__(self, movie_title, movie_year, movie_storyline, poster_image,
								trailer_youtube, movie_director, movie_rating=1):
		self.title = movie_title
		self.year = movie_year
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube
		self.director = movie_director
		self.rating = movie_rating

	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)