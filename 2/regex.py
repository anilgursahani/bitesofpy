import re

COURSE = ('Introduction 1 Lecture 01:47'
          'The Basics 4 Lectures 32:03'
          'Getting Technical!  4 Lectures 41:51'
          'Challenge 2 Lectures 27:48'
          'Afterword 1 Lecture 05:02')
TWEET = ('New PyBites article: Module of the Week - Requests-cache '
         'for Repeated API Calls - http://pybit.es/requests-cache.html '
         '#python #APIs')
HTML = ('<p>pybites != greedy</p>'
        '<p>not the same can be said REgarding ...</p>')


def extract_course_times(course=COURSE):
    """Return the course timings from the passed in
       course string. Timings are in mm:ss (minutes:seconds)
       format, so taking COURSE above you would extract:
       ['01:47', '32:03', '41:51', '27:48', '05:02']
       Return this list.
       
       
       
       
    """
    
    pattern = re.compile("\d\d:\d\d");
    theIter = re.finditer(pattern, course)
    theList = getListOfMatchedItems(theIter)
    return theList
   
    
    
def getListOfMatchedItems(iter):
    theList = []
    while True:
        try:
            
            matched = next(iter)
            theList.append(matched.string[matched.start():matched.end()])
            
        except StopIteration as S:
            break
    return theList


def get_all_hashtags_and_links(tweet=TWEET):
    """Get all hashtags and links from the tweet text
       that is passed into this function. So for TWEET
       above you need to extract the following list:
       ['http://pybit.es/requests-cache.html',
        '#python',
        '#APIs']
       Return this list.
    """
    
    exp =  "http://\S+|\#\S+"
    
    pattern = re.compile(exp)
   
    theIter = re.finditer(pattern, tweet)
    
    theList = getListOfMatchedItems(theIter)
    return theList
    
    pass


def match_first_paragraph(html=HTML):
    """Extract the first paragraph of the passed in
       html, so for HTML above this would be:
       'pybites != greedy' (= content of first paragraph).
       Return this string.
    """
    print("match first par")
    exp = r'<p>(.*?)</p>'
    pattern = re.compile(exp)
    matched = pattern.match(html)
    return(matched.group(1))
    
    
     
    pass


def main():
    courseTimes = extract_course_times()
    for courseTime in courseTimes:
        print(courseTime)
    hashTagsAndLinks = get_all_hashtags_and_links()
    for hashtagAndLink in hashTagsAndLinks:
        print(hashtagAndLink)
        
    firstPar = match_first_paragraph()
    print(firstPar)
    

if __name__ == '__main__':
    main()