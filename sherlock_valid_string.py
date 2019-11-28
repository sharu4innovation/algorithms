test = {'aabbcc':'YES', 'aabbccc':'YES', 'aabbcccc':'NO', 'aabbccd':'YES', 'aabbcd':'NO', 'abcd':'YES', 'aabcd':'YES'}

def validate_string(s):
    s = list(s)
    hash_t = {}
    for i in set(s):
        hash_t[i] = sum([i == j for j in s])
    if (len(set(hash_t.values())) == 1):
        return "YES"
    else:
        hh_t = {}
        for i in set(hash_t.values()):
            hh_t[i] = sum([i == j for j in hash_t.values()])
        if(1 in hh_t  and 1 == hh_t[1]):
            return "YES"
        elif(len(hh_t) == 2):
            x = list(hh_t.keys())
            if abs(x[0] - x[1]) == 1 and len(set(hh_t.values())) != 1:
                return "YES"
            else:
                return "NO"
        else:
            return "NO"

for case, output in test.items():
    if output == validate_string(case):
        print(case, ":",output, "PASS")
    else:
        print(case, ":",output, "FAIL")
        