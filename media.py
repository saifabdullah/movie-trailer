"""  This module contains the Video and Movie class and functions.  """

import webbrowser


class Video():

    def __init__(self, title, duration):
        self.title = title
        self.duration = (duration)


class Movie(Video):         # The main class for movie-trailer website

    valid_ratings = ["G", "PG", "PG-13", "R"]        # Global variable

    def __init__(self, title, duration, movie_storyline, poster_image_url,
                 trailer_youtube_url):
        Video.__init__(self, title, duration)
        self.storyline = movie_storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

    def show_trailer(self):

        webbrowser.open(self.trailer_youtube_url)


class Tvshow(Video):

    def __init__(self, title, duration, season, episode, tv_station):
        Video.__init__(self, title, duration)
        self.season = season
        self.episode = episode
        self.tv_station = tv_station
