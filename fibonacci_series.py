j = []
n = 8

def get_nextsum(i, j):
    if(i == 0):
        return i
    elif(i == 1):
        return i
    else:
        return sum(j[-2:])

for i in range(0,n):
    next = get_nextsum(i,j)
    j.append(next)
print(j)