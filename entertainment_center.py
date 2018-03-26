import fresh_tomatoes
import media
from media import MovieDatabase as mdb

# Creating an intance of movie_database and passing in our API key
movie_db = mdb("YOUR_API")

# A list of tmdb ids of our favorite movies
favorite_movie_ids = ["272", "19995", "155", "855", "544"]
# Adding a new movies to our list using the API search by name
favorite_movie_ids.append(movie_db.search_movie_name("the last samurai"))
favorite_movie_ids.append(movie_db.search_movie_name("ip man"))

# An array to hold our movie class instances
movie_list = []
# For each id in our favorite list get info and create class instace using API
for i in favorite_movie_ids:

    title, image, trailer = movie_db.get_movie_info(i)
    movie_list.append(media.Movie(title, image, trailer))

fresh_tomatoes.open_movies_page(movie_list)
