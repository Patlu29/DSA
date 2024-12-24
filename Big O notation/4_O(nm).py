def target(nested_list):
    total = 0
    
    for inner_list in nested_list:
        for num in inner_list:
            total += num
            
        for num in inner_list:
            total += num
            
        for num in inner_list:
            total += num
            
    return total

"""
in this case the notaions are n(3m)
--> 3nm (remove the constants)
so, The big O notation is O(nm)
"""