from collections import defaultdict
import os
from urllib.request import urlretrieve

from bs4 import BeautifulSoup 


def getHolidayMonthAndName(holiday):
    time = holiday.find("time")['datetime']
        
    year,month,day = time.split("-")
    holidayName = holiday.find("a").text.strip()
    return(month,holidayName)
    

# prep data
tmp = os.getenv("TMP", "/tmp")
page = 'us_holidays.html'
holidays_page = os.path.join(tmp, page)


urlretrieve(
    f'https://bites-data.s3.us-east-2.amazonaws.com/{page}',
    holidays_page
)

with open(holidays_page) as f:
    content = f.read()

holidays = defaultdict(list)
soup = BeautifulSoup(content, features="html.parser")

theList = soup.find_all("table", class_="list-table")
federalHolidays = []
for item in theList:
    publicHolidays = item.find_all("tr", class_="publicholiday")  
    for holiday in publicHolidays:
        (month,holidayName) = getHolidayMonthAndName(holiday)
        holidays[month].append(holidayName)
        

for item in theList:
    regularHolidays = item.find_all("tr", class_="holiday")
    for holiday in regularHolidays:
        (month,holidayName) = getHolidayMonthAndName(holiday)
        
        holidays[month].append(holidayName)
        
    
   
for item in theList:
    regionalHolidays = item.find_all("tr", class_="regional")
    
    for holiday in regionalHolidays:
        (month,holidayName) = getHolidayMonthAndName(holiday)
        holidays[month].append(holidayName)
        
 
 
   



def get_us_bank_holidays(content=content):
    """
    Receive scraped html output, make a BS object, parse the bank
       holiday table (css class = list-table), and return a dict of
       keys -> months and values -> list of bank holidays"""
    return holidays
    pass



#document.querySelector("table.list-table tr.publicholiday td:nth-child(4) a").text

#document.querySelector("table.list-table td:nth-child(2) time").getAttribute("datetime")

