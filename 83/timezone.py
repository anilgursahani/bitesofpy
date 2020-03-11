from pytz import timezone, utc
from datetime import datetime as datetime

import pytz

AUSTRALIA = timezone('Australia/Sydney')
SPAIN = timezone('Europe/Madrid')
CHICAGO = timezone('US/Central')
NY = timezone('US/Eastern')
UTC = timezone('UTC')


def what_time_lives_pybites(naive_utc_dt):

    """Receives a naive UTC datetime object and returns a two element
       tuple of Australian and Spanish (timezone aware) datetimes"""

    timesList = []
    utc = pytz.utc

    year = naive_utc_dt.year
    month = naive_utc_dt.month
    day = naive_utc_dt.day
    hour = naive_utc_dt.hour
    min = naive_utc_dt.minute
    sec = naive_utc_dt.second


    dt = datetime(year,month,day,hour,min,sec, tzinfo=pytz.UTC)


    australianTime = dt.astimezone(AUSTRALIA)
    spanishTime = dt.astimezone(SPAIN)
    timesList.append(australianTime)
    timesList.append(spanishTime)
    return tuple(timesList)
    pass

def main():

   naive_utc_dt = datetime(2018, 4, 27, 22, 55, 12)
   tupleOfTimes = what_time_lives_pybites(naive_utc_dt)
   for theTime in tupleOfTimes:
       print(theTime)




if __name__ == "__main__":
    main()