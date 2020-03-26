from collections import namedtuple

from bs4 import BeautifulSoup as Soup
import requests

PACKT = 'https://bites-data.s3.us-east-2.amazonaws.com/packt.html'



CONTENT = requests.get(PACKT).text


Book = namedtuple('Book', 'title description image link')


def get_book():
    """make a Soup object, parse the relevant html sections, and return a Book namedtuple"""
    soup = Soup(CONTENT,'lxml')
    
    title = soup.find('div', class_='dotd-title').find("h2").text
    title = title.strip()
    
    theData = soup.find('div', class_="dotd-main-book-summary float-left")
    divs = theData.find_all('div')
    descriptionText = divs[2].text.strip()
    
    aTag = soup.find('div' ,class_='dotd-main-book-image float-left').find('a')
    image = aTag.find('noscript').find('img')['src']
   
    link = soup.find('div' ,class_='dotd-main-book-image float-left').find('a')['href']
    
    book = Book(title=title, description=descriptionText, image=image, link=link)
    
    
    return book
       
    
    
    
        
    
    #attrDict = dict(attrs)
    #for attrKey in attrDict.keys():
    #    print(attrKey)
    
    pass


if __name__ == '__main__':
    book = get_book()
    


    