#!/bin/python
def repeatedString(s, n):
    def counta(a):
        sa = 0
        for i in a:
            if i == 'a':
                sa+=1
        return sa

    sa = counta(s)

    if (n % len(s)) != 0:
        sa = sa*(n/len(s)) + counta(s[:(n % len(s))])
    else:
        sa = sa*(n/len(s))
    return sa

if __name__ == '__main__':
    s = input()
    n = int(raw_input())
    result = repeatedString(s, n)
    print(result)