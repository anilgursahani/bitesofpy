import csv
from csv import DictReader 
from collections import defaultdict, namedtuple
import os
from urllib.request import urlretrieve


BASE_URL = 'https://bites-data.s3.us-east-2.amazonaws.com/'
TMP = '/tmp'

fname = 'movie_metadata.csv'
remote = os.path.join(BASE_URL, fname)
local = os.path.join(TMP, fname)

MOVIE_DATA = local
MIN_MOVIES = 4
MIN_YEAR = 1960





      
 
def get_movies_by_director():
    """Extracts all movies from csv and stores them in a dict,
    where keys are directors, and values are a list of movies,
    use the defined Movie namedtuple"""
    (filename,header) =  urlretrieve(remote, local)
    with open(filename, 'r') as csvFile:
        dictData = DictReader(csvFile)
        moviesByDirector = {}
        
        for line in dictData:
            Movie = namedtuple('Movie', 'title year score')
        
            director = line['director_name']
            Movie.title = line['movie_title']
            Movie.year = line['title_year']
            Movie.score = line['imdb_score']
        
        
            if director in moviesByDirector.keys():
           
                listOfDirectorMovies = moviesByDirector[director]
                listOfDirectorMovies.append(Movie)
            
            
            
            else:
            
                listOfDirectorMovies = []
                listOfDirectorMovies.append(Movie)
                moviesByDirector[director] = listOfDirectorMovies
            
      
    
    return moviesByDirector
        
   
    pass


def calc_mean_score(movies):
    """Helper method to calculate mean of list of Movie namedtuples,
       round the mean to 1 decimal place"""
    numMovies = len(movies)
    sum = 0
    for movie in movies:
        sum = sum + float(movie.score)
    avg = sum/numMovies
    return(round(avg,1))
        
    
    pass


def get_average_scores(directors):
     """Iterate through the directors dict (returned by get_movies_by_director),
       return a list of tuples (director, average_score) ordered by highest
       score in descending order. Only take directors into account
       with >= MIN_MOVIES"""
    
    theList = []   
    for director in directors.keys():
       
        movieList = directors[director]
        numMovies = len(movieList)
        if numMovies >= MIN_MOVIES:
            avgScore = calc_mean_score(movieList)
            AVG_SCORE = namedtuple('AVG_SCORE', ['director', 'average_score'])
            AVG_SCORE.director = director
            AVG_SCORE.average_score = avgScore
            theList.append(AVG_SCORE)
    
    
        
            
            
   
    pass

def main():
    directors = get_movies_by_director()
    get_average_scores(directors)
    
if __name__ == '__main__':
    main()

    