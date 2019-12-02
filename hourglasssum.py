def hourglassSum(arr):
    r = len(arr)
    c = len(arr[0])
    max_hsum  = 0
    for i in range(0, r - 2):
        for j in  range(0, c - 2):
            hsum = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            if i == 0 and j == 0:
                max_hsum = hsum
            if hsum > max_hsum:
                max_hsum = hsum
    return max_hsum    
        

if __name__ == '__main__':
    arr = []
    for _ in xrange(6):
        arr.append(map(int, raw_input().rstrip().split()))
    result = hourglassSum(arr)
    print(result)