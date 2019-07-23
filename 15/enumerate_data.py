names = 'Julian Bob PyBites Dante Martin Rodolfo'.split()
countries = 'Australia Spain Global Argentina USA Mexico'.split()


def enumerate_names_countries():
    """Outputs:
       1. Julian     Australia
       2. Bob        Spain
       3. PyBites    Global
       4. Dante      Argentina
       5. Martin     USA
       6. Rodolfo    Mexico"""
       
    index = 0
    for name in names:
        country = countries[index]
        seqNum = index + 1
        print("{0}. {1:11s}{2}".format(seqNum,name,countries[index]))
        index+= 1
        
    
         
if __name__ == '__main__':
    enumerate_names_countries()
   


