from data_persistence import DataPersistence
from movie import Movie


class MovieManagement:
    def __init__(self):
        self._movies = []
        self._file = DataPersistence()
        for row in self._file._read_data:
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
            if movie_id == movie.get_id():
                self._movies.remove(movie)

    def find_movie(self, option, entry):
        if option == 0:
            for movie in self._movies:
                if entry == movie.get_id():
                    return movie
        elif option == 1:
            for movie in self._movies:
                if entry == movie.get_name():
                    return movie
        return False
                
    def get_movies(self):
        return self._movies
    
    def save(self):
        self._file.save(self._movies)