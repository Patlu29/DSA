def resulr(dict1, dict2): # --> n, m
    keys1 = sorted(dict1.keys()) # --> n log2(n)
    keys2 = sorted(dict2.keys()) # --> m log2(m)
    
    process = keys1 + keys2 # --> O(n + m)
    results = set()
    
    while len(process) > 0:
        element = process.pop(0) # --> process.pop(0) takes O(p) 'p' is size of the list----pop() method takes O(k^2) 'k'is total number of elements processed
        results.append(element) # --> constant O(1)
        
        if len(element) == 1:
            continue
        
        process.append(element[:-1]) # --> O(L) 'L' is the average string length
        
    return results

"""
Time complexity:
O(n log2(n) + m log2(m) + (n + m)k)
"""
        