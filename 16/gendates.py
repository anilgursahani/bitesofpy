from datetime import datetime
from datetime import timedelta

PYBITES_BORN = datetime(year=2016, month=12, day=19)


def gen_special_pybites_dates():
    currentYearDT = PYBITES_BORN
    dt = PYBITES_BORN ;
    
    td100 = timedelta(100,0,0)
    td365 = timedelta(365, 0, 0)
    
    while True:
        
        for idx in range(3):
            dt += td100
            print(dt)
            yield(dt)
            
        currentYearDT = currentYearDT + td365
        print(currentYearDT)
        yield(currentYearDT)
        dt += td100
        print(dt)
        yield(dt)
       
            
    
    
    pass  
        
    
 
