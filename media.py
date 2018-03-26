import webbrowser
import requests
import json


class Movie():
    """ This class provides a way to store movie related information"""

    def __init__(self, title, poster_image, trailer_youtube):
        self.title = title
        self.poster_image_url = poster_image
        self.trailer_youtube_key = trailer_youtube

    def show_trailer(self):
        """This method will open the youtube trailer page in the web browser"""
        webbrowser.open("https://www.youtube.com/" + self.trailer_youtube_key)


class MovieDatabase():
    """This class uses the movie database API to collect movie information"""

    def __init__(self, api_key):
        self.api_key = api_key
        self.movie_list = []

    def search_movie_name(self, movie_name):
        """This function will take a movie name and return first results id"""

        res = requests.get(
                    "https://api.themoviedb.org/3/search"
                    + "/movie?include_adult=true&page=1&query="
                    + movie_name +"&language=en-US&api_key="
                    + self.api_key)

        data = res.json()
        return str(data["results"][0]["id"])

    def get_movie_info(self, movie_id):
        """This function will take a movie id and will reutnr all needed
           information to create a movie instance"""

        poster_base_path = "https://image.tmdb.org/t/p/original/"
        res = requests.get(
                    "https://api.themoviedb.org/3/movie/"
                    + movie_id + "?language=en-US&api_key="
                    + self.api_key)

        data = res.json()
        title = data["title"]
        poster_image = poster_base_path + data["poster_path"]

        res = requests.get(
                    "https://api.themoviedb.org/3/movie/"
                    + movie_id + "/videos?language=en-US&api_key="
                    + self.api_key)
        data = res.json()
        youtube_key = data["results"][0]["key"]

        return title, poster_image, youtube_key
