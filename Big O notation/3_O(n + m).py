def result(nums1,nums2):
    result = [] # --> 1
    
    for num in nums1: # --> n
        result.append(num) # --> 1
        
    for i, num in enumerate(nums2): # --> m
        if i >= len(result): # --> 1
            result.append(1) # --> 1
        result[i] *= 2 # --> 1
        
    return result# --> 1




"""
1 + n + 3m + 1 get rid of all constants
--> n+m
So, the big O notation is O(n +m)
"""