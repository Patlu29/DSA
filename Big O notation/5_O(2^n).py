import time
# big O notaion on recursive function
start = time.perf_counter()
def fibonacci(n):
    if n <= 0:
        return 0 
    if n == 1:     # these 4 steps are constant
        return 1
    
    f1 = fibonacci(n - 1) # --> n
    f2 = fibonacci(n - 2) # --> n
    
    return f1 + f2
end = time.perf_counter()

print(end - start)
print(fibonacci(10))

"""
in this notation the function recursive so, n * n --> 2 ^ n its run like tree structure ex(n = 5)
                    5
                  /   \
                 4     3
                / \   /  \
               3   2 2    1
              / \
             2   1
    tihs is the work flow of this recursive function 
    so, the big O notation is O(2^n)
"""