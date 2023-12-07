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
        for movie in self._movies:
            if movie_id == movie._movie_id:
                movie.set_movie_name(movie_name)
                movie.set_country_name(country_name)
                movie.set_duration(duration)
                movie.set_genre(genre)
                movie.set_rating(rating)

    def delete(self, movie_id):
        for movie in self._movies:
            if movie_id == movie.get_movie_id():
                self._movies.remove(movie)

    def find_movie(self, option, entry):
        if option == 0:
            for movie in self._movies:
                if entry == movie.get_movie_id():
                    return movie
        elif option == 1:
            for movie in self._movies:
                if entry == movie.get_movie_name():
                    return movie
        return False
                
    def get_movies(self):
        return self._movies
    
    def save(self):
        self._file.save(self._movies)

    def sort(self):
        self._movies = sorted(self._movies, key=lambda movie: movie._movie_id)