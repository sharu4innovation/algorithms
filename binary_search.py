def iterative_binary_search(A,n,T):
    l = 0
    r = n-1
    while l <= r:
        m = (l + r)//2
        if A[m] < T:
            l = m + 1
        elif A[m] > T:
            r = m - 1
        else:
            return m
    return "Not Found"
            

n = 10
A = range(0,n)
T = 6
print("Result of Iterative Binary Search: ",iterative_binary_search(A,len(A),T))

def recursive_binary_search(A, l,r,x):
    if r >= l:
        m = (l+r)//2
        if A[m] < x:
            return recursive_binary_search(A,m+1,r,x)
        elif A[m] > x:
            return recursive_binary_search(A,l,m-1,x)
        else:
            return ("Found",m)
    else:
        return ("Not Found", -1)

n = 10
A = range(0,n)
T = 23
print("Result of Recursive Binary Search: ",recursive_binary_search(A,0,n-1,T))