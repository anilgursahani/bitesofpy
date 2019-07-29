cars = {
    'Ford': ['Falcon', 'Focus', 'Festiva', 'Fairlane'],
    'Holden': ['Commodore', 'Captiva', 'Barina', 'Trailblazer'],
    'Nissan': ['Maxima', 'Pulsar', '350Z', 'Navara'],
    'Honda': ['Civic', 'Accord', 'Odyssey', 'Jazz'],
    'Jeep': ['Grand Cherokee', 'Cherokee', 'Trailhawk', 'Trackhawk']
}


def get_all_jeeps(cars=cars):
    """return a comma  + space (', ') separated string of jeep models
       (original order)"""
    jeepList = cars['Jeep']
    numJeeps = len(jeepList)
    jeepString = ""
    for idx in range(numJeeps-1):
        jeep = jeepList[idx]
        jeepString = jeepString + jeep + ", "
    
    jeep = jeepList[numJeeps-1]
    jeepString = jeepString + jeep
    return jeepString
        
       
       
    pass

def __getManufacturers__():
    return cars.keys()

def get_first_model_each_manufacturer(cars=cars):
    """return a list of matching models (original ordering)"""
    firstModels = []
    manufacturers = __getManufacturers__()
    for manufacturer in manufacturers:
        models = cars[manufacturer]
        firstModels.append(models[0])
    
    return firstModels
        
        
       
    pass


def get_all_matching_models(cars=cars, grep='trail'):
    """return a list of all models containing the case insensitive
       'grep' string which defaults to 'trail' for this exercise,
       sort the resulting sequence alphabetically"""
    manufacturers = __getManufacturers__()
   
    models = []
    for manufacturer in manufacturers:
        manufacturerModels = cars[manufacturer]
        for manufacturerModel in manufacturerModels:
            models.append(manufacturerModel)
    modelsFound = []
    for model in models:
        
        
        modelLower = model.lower()
        
       
        
        if grep.lower() in modelLower:
            
            modelsFound.append(model)
    modelsFoundSorted= sorted(modelsFound)
    
   
    return modelsFoundSorted
        
     
    pass


def sort_car_models(cars=cars):
    """return a copy of the cars dict with the car models (values)
       sorted alphabetically"""
    manufacturers = __getManufacturers__()
    carsSortedDict = {}
    for manufacturer in manufacturers:
        manufacturerModels = cars[manufacturer]
        manufacturerModelsSorted = sorted(manufacturerModels)
        carsSortedDict[manufacturer] = manufacturerModelsSorted
        
    return carsSortedDict
        
        
        
        

    pass

if __name__ == '__main__':
    jeeps = get_all_jeeps()
    print(jeeps)
    firstModels = get_first_model_each_manufacturer()
    for firstModel in firstModels:
        print(firstModel)
        
    matchingModels = get_all_matching_models()
    for matchingModel in matchingModels:
        print(matchingModel)