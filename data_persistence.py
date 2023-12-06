import csv

class DataPersistence:
    def __init__(self):
        self.read_dictionary = []
        with open('movie_collection.csv', 'r') as f:
            for row in csv.DictReader(f):
                self.read_dictionary.append(row)

    def save(self, movies_list):
        with open('movie_collection.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow(['movie_id','movie_name','country_name','duration','genre','rating'])
            for movie in movies_list:
                writer.writerow([movie._movieid, movie._name, movie._country_name, movie._duration, movie._genre, movie._rating])

dp = DataPersistence()
for row in dp.read_dictionary:
    for item in row:
        print(type(item))

    
    
    
    
