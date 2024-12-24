import time
def log(n):
    if n == 0 :
        return 
    
    print(n)
    log(round(n / 2)) # it reduces a value into minimun so its a log 2 based n --> log2(n)
    """
    in this function it work recursively and it reduces the time to minimum by dividing a n into 2
    so, the big O notion is O(log2(n))
    """
    
print(log(10000))