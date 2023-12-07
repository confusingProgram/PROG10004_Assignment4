class Movie:
    def __init__(self, movie_id, movie_name, country_name, duration, genre, rating):
        self._movie_id = movie_id
        self._movie_name = movie_name
        self._country_name = country_name
        self._duration = duration
        self._genre = genre
        self._rating = rating
    
    def get_movie_id(self):
        return self._movie_id
    
    def _set_movie_id(self, new):
        self._movie_id = new
    
    def get_movie_name(self):
        return self._movie_name
    
    def set_movie_name(self, new):
        self._movie_name = new

    def get_country_name(self):
        return self._country_name
    
    def set_country_name(self, new):
        self._country_name = new

    def get_duration(self):
        return self._duration
    
    def set_duration(self, new):
        self._duration = new

    def get_genre(self):
        return self._genre
    
    def set_genre(self, new):
        self._genre = new

    def get_rating(self):
        return self._rating
    
    def set_rating(self, new):
        self._rating = new
    
    


