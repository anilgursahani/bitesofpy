import re
def remove_punctuation(input_string):
    """Return a str with punctuation chars stripped out"""
    pattern = ('\W')
    nonWordCharPat = re.compile(pattern)
    pattern = ('\s')
    wsPat = re.compile(pattern)
    nonWordChars = re.findall(nonWordCharPat,input_string);
    wsChars = re.findall(wsPat, input_string);
    charList = [aChar for aChar in input_string if aChar in wsChars or aChar not in nonWordChars]
    newString = "".join(charList)
    return newString
    pass