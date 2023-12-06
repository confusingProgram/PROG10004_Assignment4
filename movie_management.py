from data_persistence import DataPersistence
from movie import Movie

"""
class Movie:
    def __init__(self, movie_id, movie_name, country_name, duration, genre, rating):
        self._movie_id = movie_id
        self._movie_name = movie_name
        self._country_name = country_name
        self._duration = duration
        self._genre = genre
        self._rating = rating
    pass
"""

class MovieManagement:
    def __init__(self):
        self._movies = []
        self._file = DataPersistence()
        for row in self._file.read_dictionary:
            self._movies.append(Movie(row['movie_id'], row['movie_name'], row['country_name'],
                                      row['duration'], row['genre'], row['rating']))
        

    def add(self, movie_id, movie_name, country_name, duration, genre, rating):
        self._movies.append(Movie(movie_id, movie_name, country_name, duration, genre, rating))

    def update(self, movie_id, movie_name, country_name, duration, genre, rating):
        newList = []
        for movie in self._movies:
            if movie_id == movie._movie_id:
                newList.append(Movie(movie_id, movie_name, country_name, duration, genre, rating))
            else:
                newList.append(movie)
        self._movies = newList

    def delete(self, movie_id):
        for movie in self._movies:
            if movie_id == movie._movie_id:
                self._movies.remove(movie)

    def find_movie(self, option, movie_id, movie_name):
        if option == 0:
            for movie in self._movies:
                if movie_id == movie._movie_id:
                    return movie
        elif option == 1:
            for movie in self._movies:
                if movie_name == movie._movie_name:
                    return movie
                
    def get_movies(self):
        return self._movies
    
    def save(self):
        self._file.save(self._movies)

MovieManagement()