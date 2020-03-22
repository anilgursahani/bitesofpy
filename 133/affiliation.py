def generate_affiliation_link(url):
    '''
    lastPartOfAffiliation = "?tag=pyb0f-20"
    amazonPart = "https://www.amazon.com/"
    affiliation = "http://www.amazon.com/"
    lastSlashIdx = url.rfind("/")
    urlToProcess = url[0:lastSlashIdx]
    print(f'Url to process is {urlToProcess}')
    amazonPartLen = len(amazonPart)
    restOfUrl = urlToProcess[amazonPartLen:]
    print(f'rest of url is {restOfUrl}')
    startDPIdx = restOfUrl.find("dp")
    dpPart = restOfUrl[startDPIdx:]
    affiliation = affiliation + dpPart + lastPartOfAffiliation
    
    
    return affiliation
    '''
    affiliation = "http://www.amazon.com/dp/"
    
    partsOfUrl = url.split('/')
    for idx, urlPart in enumerate(partsOfUrl):
        
        if urlPart.startswith('dp'):
            break
    followingDP = partsOfUrl[idx+1].rstrip("/")
    affiliation = affiliation + followingDP
    
    affiliation = affiliation + "/?tag=pyb0f-20"
    return affiliation
       
        
    
   
def main():
    
    urls = ["https://www.amazon.com/War-Art-Through-Creative-Battles/dp/1936891026/?keywords=war+of+art",
            "https://amazon.com/War-Art-Through-Creative-Battles/dp/1936891026/ref=sr_1_1",
            "https://www.amazon.es/War-Art-Through-Creative-Battles/dp/1936891026/?qid=1537226234",
            "https://www.amazon.co.uk/Pragmatic-Programmer-Andrew-Hunt/dp/020161622X",
            "https://www.amazon.com.au/Python-Cookbook-3e-David-Beazley/dp/1449340377/"]
    for url in urls:
        print(url)
        affliation = generate_affiliation_link(url)
        print(f'result is {affliation}')
        print()
    
    
    
    
if __name__ == '__main__':
    main()