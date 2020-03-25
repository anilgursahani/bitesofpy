from collections import defaultdict

# fake data from https://www.mockaroo.com
data = """last_name,first_name,country_code
Watsham,Husain,ID
Harrold,Alphonso,BR
Apdell,Margo,CN
Tomblings,Deerdre,RU
Wasielewski,Sula,ID
Jeffry,Rudolph,TD
Brenston,Luke,SE
Parrett,Ines,CN
Braunle,Kermit,PL
Halbard,Davie,CN"""

def createCountriesListFromData(data):
    personsCountryData = data.splitlines(keepends=False)
    personsCountryData = personsCountryData[1:]
    
    
    for personData in personsCountryData:
        yield personData
           

def group_names_by_country(data: str = data) -> defaultdict:
   
    countries = defaultdict(list)
    personsCountryData = createCountriesListFromData(data)
    for personData in personsCountryData:
        lastname,firstname,country = personData.split(",")
        name = f'{firstname} {lastname}'
        countries[country].append(name)
    return countries
           
        
    
    
        
    
    # you code
    

def main():
    countries = group_names_by_country()
    print(repr(countries))
    
if __name__ == '__main__':
    main()
    