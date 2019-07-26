from datetime import datetime
from datetime import timedelta

NOW = datetime.now()


class Promo(object):
    
    def __init__(self, name, expireTime):
        self.__name = name
        self.__expired = expireTime
   
    
    
    
    
    @property
    def expiredTime(self):
        return self.__expired
    
    
    @property
    def expired(self):
        if NOW >= self.__expired:
            expired = True
        else:
            expired = False
        
        return expired
        
        
    
    
        
        
    pass

def main():
    past_time = NOW - timedelta(seconds=3)
    twitter_promo = Promo('twitter', past_time)
    twitterTimeExpired = twitter_promo.expiredTime
    print(twitterTimeExpired)
    
    futureTime = NOW + timedelta(seconds=180)
    newsTimePromo = Promo('newstime', futureTime)
    newsTimeExpired = newsTimePromo.expiredTime
    print (newsTimeExpired)
    
    expired = twitter_promo.expired
    print ("Twitter expired is {}".format(expired))
    expired = newsTimePromo.expired
    print ("News time promo expired is {}".format(expired))
    
    
    
  
    
    
    
    
if __name__ == '__main__':
    main()