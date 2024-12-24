def total(num):
    total_num = 0 # variable takes one operation --> 1
    
    for number in num: # for loop takes a n operation --> n
        total_num += number # it takes one operation--> 1
    
    return total_num

print(total([1,2,3,4,5,6,7]))

"""
in this case n + 2 so we remove a constant so, this is O(n)
"""