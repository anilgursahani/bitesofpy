IMPOSSIBLE = 'Mission impossible. No one can contribute.'


def max_fund(village):
    """Find a contiguous subarray with the largest sum."""
    runningSumAccumulated = []
    
    # Hint: while iterating, you could save the best_sum collected so far
    # return total, starting, ending
    
    # Assume the mayor is so generous that if he collects money and runs into household
    # mayor gives amount household needs or how much mayor can afford to give. Find the last
    # house mayor's aide should tell mayor to get money from
    # so mayor has collected maximum and does not give
    # any of it away
    # Start with creating a running sum total for the houses in the village list
    #
    
    runningSum = 0
    for amount in village:
        runningSum = runningSum + amount
        if runningSum < 0:
            runningSum = 0
        runningSumAccumulated.append(runningSum)
       
        
    # Now starting from the end of the list and going to the start of the list find the house
    # at which maximum amount was accumulated
    
    idx = len(runningSumAccumulated) - 1
    maxAccumulated  = 0
    
    while(idx >= 0):
        amount = runningSumAccumulated[idx]
        if amount >= maxAccumulated:
            maxAccumulated = amount
            idxToLastHouse = idx
        idx = idx - 1
        
   
        
    # now we have the max accumulated and the index to the house zero based where collected most from
    
    # Now determine the house from where to start collecting
    currentIdx = idxToLastHouse - 1
    while(currentIdx >= 0):
        if runningSumAccumulated[currentIdx] == 0:
            idxToFirstHouse = currentIdx + 1
            break
        else:
            currentIdx -= 1
    
    if maxAccumulated == 0:
        print(f'{IMPOSSIBLE}' )
        returnedTuple = (0,0,0)
    else:
        returnedTuple = (maxAccumulated, idxToFirstHouse+1, idxToLastHouse+1)
        
    return returnedTuple
        
        
        
        
  
    pass


def main():
    returnList = max_fund ([0, 1, -1, -5, 0, 4, -3, -2])
    for item in returnList:
        print(item)
    
    

if __name__ == '__main__':
    main()
    
