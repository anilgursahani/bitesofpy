def rotate(string, n):
    """Rotate characters in a string.
       Expects string and n (int) for number of characters to move.
    """
    front = string
    back = ""
    slen = len(string)
    if n > 0:
        back = string[0:n]
        front = string[n:slen]
        returnString = front + back
        print ("Positive, string is {} return string is {}".format(string, returnString))
    elif n < 0:
        
        back = string[:n]
        front = string[n:slen]
        returnString =  front + back
        print ("Negative, string is {} return string is {}".format(string, returnString))
        
        
        
    
    return returnString
        
        
        
    
    pass