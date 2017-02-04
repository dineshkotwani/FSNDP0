''' This file contains Movie class implementation. '''
import webbrowser


class Movie():
    ''' Movie Class is the class created to store movie details. '''
    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        '''Method to initialise Movie Class
               Parameters:
               movie_title (str): Instance variable to save movie title
               movie_storyline (str): Instance variable to save movie storyline
               poster_image (str): Instance variable to save movie poster image
               trailer_youtube (str): Instance variable to save trailer URL
        '''
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        ''' Instance method to show movie trailer. '''
        webbrowser.open(self.trailer_youtube_url)
