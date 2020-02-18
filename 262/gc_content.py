def calculate_gc_content(sequence):
    """
    Receives a DNA sequence (A, G, C, or T)
    Returns the percentage of GC content (rounded to the last two digits)
    """
    
    # first convert sequence to lower case
    
    sequenceLowerCase = sequence.lower()
    print("Sequence is {}".format(sequenceLowerCase))
    countAs = sequenceLowerCase.count("a",0)
    countGs = sequenceLowerCase.count("g",0)
    countCs = sequenceLowerCase.count("c",0)
    countTs = sequenceLowerCase.count("t",0)
    
    countOfAGCT = countAs + countGs + countCs + countTs
    countOfCAndG = countCs + countGs
    percentageOfGC = float(countOfCAndG)/(float(countOfAGCT))*100
    percentageOfGCRounded = round(percentageOfGC,2)
    return percentageOfGCRounded
    
    
    
    
    
    pass