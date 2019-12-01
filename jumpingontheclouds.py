def jumpingOnClouds(arr):
    jump = 0
    i = 0
    while i < len(arr) - 1:
        if( i+2 == len(arr) or arr[i + 2] == 1):
            i = i + 1
            jump = jump + 1
        else:
            i = i + 2
            jump = jump + 1
    return jump
    


if __name__ == '__main__':
    n = int(raw_input())

    c = map(int, raw_input().rstrip().split())

    result = jumpingOnClouds(c)
    print(result)