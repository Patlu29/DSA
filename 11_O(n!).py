import time
def result(n):
    st = time.perf_counter()
    if n <= 0:
        return 1
    
    total = 0
    
    for _ in range(n):
        total += result(n - 1)
    
    sp = time.perf_counter()  
    ttime = sp - st  
    
    #return total
    return ttime

ans = result(int(input("Enter a number: ")))
print(ans)