def sockMerchant(n, ar):
    paired = {}
    counter = 0

    for i in ar:
        if paired.get(i):
            paired[i] = paired[i] + 1
        else:
            paired[i] = 1

    for i in paired.values():
        print(i)
        counter = counter + i//2
    return counter

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    ar = list(map(int, input().rstrip().split()))
    result = sockMerchant(n, ar)
    print(result)
