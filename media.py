import webbrowser

class Movie():
 """This program is a web page represent my favorite movies I watched recently. you also are able to watch the trailer of each by clicking on poster image"""
 def __init__(self,movie_title,movie_storyline,poster_image,trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
 def show_trailer(self):
		"""This function will open the movie's trailer in browser"""
        webbrowser.open(self.trailer_youtube_url)
		

