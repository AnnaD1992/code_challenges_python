from typing import List, Any
original_list = [1,2,3,4,5,6]

def reverse(myList: List[Any])->List[Any]:
    
    for i in  range( len(myList)//2): # This part was important for the reverse, instead of going through the whole list
        #Solution # 1
        # temp = myList[i]
        # myList[i] = myList[len(myList)-i-1]
        # myList[len(myList)-i-1] = temp
    
        # Solution # 2
         myList[i], myList[len(myList) - i - 1] = myList[len(myList) - i - 1], myList[i] ## Unpacking tuple
        #The key is that the tuple is created before any assignments are made. 
        #This means that the original values of myList[i] and myList[len(myList) - i - 1] are safely stored in the tuple.

        
    return myList
    
print("Original List: ", original_list)
print("Reversed List: ", reverse(original_list))