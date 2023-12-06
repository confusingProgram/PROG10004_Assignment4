class Movie:
    def __init__(self, movie_id, movie_name, country_name, duration, genre, rating):
        self._movie_id = movie_id
        self._movie_name = movie_name
        self._country_name = country_name
        self._duration = duration
        self._genre = genre
        self._rating = rating
    
    def get_id(self):
        return self._movie_id
    
    def get_name(self):
        return self._movie_name

    def get_country(self):
        return self._country_name

    def get_duration(self):
        return self._duration

    def get_genre(self):
        return self._genre

    def get_rating(self):
        return self._rating


