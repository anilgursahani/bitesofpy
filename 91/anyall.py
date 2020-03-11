import re
VOWELS = 'aeiou'
PYTHON = 'python'



def contains_only_vowels(input_str):
    """Receives input string and checks if all chars are
       VOWELS. Match is case insensitive."""
    exp = '[^aeiou]'
    pattern = re.compile(exp)
    allLower = input_str.lower()
    matched = pattern.findall(allLower)
    if len(matched) == 0:
        return True
    else:
        return False


    pass


def contains_any_py_chars(input_str):
    """Receives input string and checks if any of the PYTHON
       chars are in it. Match is case insensitive."""

    exp = '[python]'
    pattern = re.compile(exp)
    alllower = input_str.lower()
    matched = pattern.findall(alllower)
    if len(matched) > 0:
        return True
    else:
        return False




    pass


def contains_digits(input_str):
    """Receives input string and checks if it contains
       one or more digits."""

    exp = '\d+'
    pat = re.compile(exp)
    matched = pat.findall(input_str)
    if len(matched) > 0:
        return True
    else:
        return False

    pass

def main():
    contains_only_vowels("a12ZA")

if __name__ == '__main__':
    main()