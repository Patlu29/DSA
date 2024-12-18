def result(nums):
    results = [1 for _ in range(len(nums))] # --> n
    for i, num1 in enumerate(nums): # --> n
        for num2 in nums: # --> n
            if num1 == num2: # --> 1
                continue # --> 1
            results[i] *= 2 # --> 1
            
    return results # --> 1

b = result([1,2,3,4,5,6,7,8,9])
print (b)

"""
In this case the notation is n + n(3n) --> n + 3n^2 so, the Big O notation is O(n^2)
"""
    