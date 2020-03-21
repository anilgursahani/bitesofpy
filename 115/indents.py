import re
def count_indents(text):
    pattern = re.compile(r"(\s+)")
    matched = pattern.match(text)
    if matched:
       matchedText = matched.group(0)
       count = matchedText.count(" ",0)
    else:
        count = 0
   
    return count
    pass

def main():
    count = count_indents("     Five Spaces")
    print(f'Count is {count}')
    count = count_indents("\t\tTwoTabs")
    print(f'Count is {count}')
    count = count_indents("String  ")
    print(f'Count is {count}')
    
    

if __name__ == '__main__':
   
    main()