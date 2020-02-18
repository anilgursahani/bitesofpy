from enum import Enum


class Equality(Enum):
    SAME_REFERENCE = 4
    SAME_ORDERED = 3
    SAME_UNORDERED = 2
    SAME_UNORDERED_DEDUPED = 1
    NO_EQUALITY = 0


def __compareLists__(l1,l2):
    matchResult = True
    if len(l1) != len(l2):
        matchResult = False
        return matchResult
    for idx, value in enumerate(l1):
        if value != l2[idx]:
            matchResult = False
            break
    
    return matchResult
            
    
   
    
    
def check_equality(list1, list2):
    """Check if list1 and list2 are equal returning the kind of equality.
       Use the values in the Equality Enum:
       - return SAME_REFERENCE if both lists reference the same object
       - return SAME_ORDERED if they have the same content and order
       - return SAME_UNORDERED if they have the same content unordered
       - return SAME_UNORDERED_DEDUPED if they have the same unordered content
         and reduced to unique items
       - return NO_EQUALITY if none of the previous cases match"""
    
    
    
    if list1 is list2:
        
        return Equality.SAME_REFERENCE
    
    list1Len = len(list1)
    list2Len = len(list2)
    
    if  list1Len == list2Len:
        match = __compareLists__(list1,list2)
        if match:
          
            return Equality.SAME_ORDERED
        list1Sorted = sorted(list1)
        list2Sorted = sorted(list2)
        match = __compareLists__(list1Sorted,list2Sorted)
        if match:
           
            return Equality.SAME_UNORDERED
        else:
           
            return Equality.NO_EQUALITY
    
    else:
        list1UniqueItems = sorted(list(set(list1)))
        list2UniqueItems = sorted(list(set(list2)))
        match = __compareLists__(list1UniqueItems, list2UniqueItems)
        if match:
           
            return Equality.SAME_UNORDERED_DEDUPED
        else:
           
            return Equality.NO_EQUALITY
        
     
       
    
    

    
    
   
        
        
     
     
    
       
    
    
   
    
  
    
    
    
    
        
        
    
    
    
    
        
        
        
    
       
      
      
       
    pass