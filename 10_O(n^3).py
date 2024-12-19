def result (nums):
    sum_to_end = [] 
    count = 0
    
    for i in range(len(nums)): # --> n complexity
        num1 = nums[i]
        sum_to_end.append(0)
        
        for j in range(i + 1, len(nums)): # --> n complexity
            num2 = nums[j]
            sum_to_end[i] += num2
            
            for _ in sum_to_end: # --> n complexity
                count += 1
                print(count)
    
ans = result([1, 2, 3, 4, 5,6,7])
print(ans)
ans.sort()
print(f"sorted: {ans}")

"""
the time complexity of each loop is n, n, and n respectively.
so, the time complexity of the function is O(n^3)    
"""