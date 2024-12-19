def result(strings):
    for i,string in enumerate(strings): # this takes n complexity
        digits = 0
        
        for char in string :
            if char in [str(i) for i in range(0,10)]: # this is a constant bcoz it iterates 0-9(10)
                digits += 1
                print(digits)
                
        if digits >= len(string) / 2:
            strings[i] = sorted(strings[i]) # sorting method defaultly take log2(n) complexity
            print(strings)
            
    return strings
   
print(result(["HELLO"]))

"""
the time complexity of this code is O(n(k log2(k)))
space complexity is O(n * k)    
"""