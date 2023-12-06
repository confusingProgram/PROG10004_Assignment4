import csv

class DataPersistence:
    def __init__(self):
        self._read_data = []
        with open('movie_collection.csv', 'r') as f:
            for row in csv.DictReader(f):
                self._read_data.append(row)

    def save(self, movies_list):
        with open('movie_collection.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow(['movie_id','movie_name','country_name','duration','genre','rating'])
            for movie in movies_list:
                writer.writerow([movie.get_id(), movie.get_name(), movie.get_country_name(), movie.get_duration(), movie.get_genre(), movie.get_rating()])
    