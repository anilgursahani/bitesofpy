import os
import urllib.request

TMP = os.getenv("TMP", "/tmp")
DATA = 'safari.logs'
SAFARI_LOGS = os.path.join(TMP, DATA)
PY_BOOK, OTHER_BOOK = '🐍', '.'

urllib.request.urlretrieve(f'https://bites-data.s3.us-east-2.amazonaws.com/{DATA}', SAFARI_LOGS)
  

def getLine():
    with open(SAFARI_LOGS, 'r') as safariLogs:
        gotData = True
        while gotData:
            line=safariLogs.readline()
            if len(line) == 0:
                gotData = False
                
            else:
                yield line

            
               
                
                
    
    
    

def main():
    
    print("ok")


def create_chart():
    flagToCheckPrevLine = "sending to slack channel"
    currentDate="00-00"
    
    dataToOutput = ""
    previousLine = "Gibberish" # Initialize previous line with gibberish so we have a starting point
    for line in getLine():
        
        if flagToCheckPrevLine in line:
            previousLine = previousLine.lower()
            theDate = previousLine[:5]
            if theDate != currentDate: # if date changed and we have data from before output what we have 
                if len(dataToOutput) > 0:
                    print(dataToOutput)
                dataToOutput = f'{theDate} '  # Get the date
                currentDate = theDate
            if "python" in previousLine:
                dataToOutput = f'{dataToOutput}{PY_BOOK}'
            else:
                dataToOutput = f'{dataToOutput}{OTHER_BOOK}'
        previousLine = line
    if len(dataToOutput) > 0:
        print(dataToOutput)
        
                    
                
                
            
                
        
    
   
if __name__ == '__main__':
    create_chart()
    