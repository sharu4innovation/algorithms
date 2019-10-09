arr = [0,1,2,3,4,5]
t = 5
sm = 0

cur_sum = arr[0]
start = 0
i = 0
n = len(arr)
while(i < n ):
    while(cur_sum > t and start < i-1):
        cur_sum = cur_sum - arr[start]
        start +=1
    if(cur_sum == t):
        break
    if(i < n):
        cur_sum += arr[i]
    i+=1