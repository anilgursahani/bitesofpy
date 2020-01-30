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
urlretrieve(remote, local)

MOVIE_DATA = local
MIN_MOVIES = 4
MIN_YEAR = 1960

Movie = namedtuple('Movie', 'title year score')


def get_movies_by_director():
    """Extracts all movies from csv and stores them in a dict,
    where keys are directors, and values are a list of movies,
    use the defined Movie namedtuple"""
    
    (filename,header) =  urlretrieve(remote, local)
    with open(filename, 'r') as csvFile:
        dictData = DictReader(csvFile)
        moviesByDirector = {}
        
        for line in dictData:
          
        
            director = line['director_name']
            movieTitle = line['movie_title']
            movieYear = line['title_year']
            
            movieScore = line['imdb_score']
            
            
            if movieYear.isdigit():
                yearOfMovie = int(movieYear)
            else:
                yearOfMovie = 0
               
                
            theMovie = Movie(movieTitle, movieYear, movieScore)
            
            
            
            if yearOfMovie  > MIN_YEAR:
                if director in moviesByDirector.keys():
                   
                    listOfDirectorMovies = moviesByDirector[director]
                    listOfDirectorMovies.append(theMovie)
                else:
                    listOfDirectorMovies = []
                    listOfDirectorMovies.append(theMovie)
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

AVG_SCORE = namedtuple('AVG_SCORE', ['director', 'average_score'])

def get_average_scores(directors):
    """Iterate through the directors dict (returned by get_movies_by_director),
       return a list of tuples (director, average_score) ordered by highest
       score in descending order. Only take directors into account
       with >= MIN_MOVIES"""
       
    directorList = []   
   
    for director in directors.keys():
       
        movieList = directors[director]
        directorAndScore = []
        numMovies = len(movieList)
        if numMovies >= MIN_MOVIES:
            avgScore = calc_mean_score(movieList)
            theAverageScore = AVG_SCORE(director, avgScore)
            
            
            directorList.append(tuple(theAverageScore))
            
        
    DoSortDirectorList(directorList)
    return directorList
    
    pass

'''
 This function sorts the list of directors that contains list of tuples (director , average_score) ordered by highest score in descending order.

'''

def DoSortDirectorList(theList):
    numItems = len(theList)
    for posToSetIdx in range(numItems-1):
        for j in range(posToSetIdx+1,numItems):
            posToSetItem = theList[posToSetIdx]
            jItem = theList[j]
            posToSetAvgScore = posToSetItem[1]
            jItemAvgScore = jItem[1]
            if jItemAvgScore > posToSetAvgScore:
                temp = theList[posToSetIdx]
                theList[posToSetIdx] = theList[j]
                theList[j] = temp
            
   
    