def search(lst, search_lst):
    max_value = max(lst) # --> n
    
    for value in search_lst: # --> m
        if max_value == value: # --> 1
            return True
        
    return False
"""
In this case the max_value search through the list for find the max number so that is n
the for loop is search the value is in the list or not (2.possibilities)
    1. we got a value in first iteration
    2. else it take a n number of iteration 
others are constant
so, the notation equation is (n+m)
it is a big O notaion  O(n + m)
"""