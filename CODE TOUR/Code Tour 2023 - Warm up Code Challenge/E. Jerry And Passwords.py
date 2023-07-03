from collections import defaultdict


def check():
    for i in range(10):
        if count[str(i)] > 1:
            return False
    return True


for _ in range(int(input())):
    s = input()
    count = defaultdict(lambda: 0)
    for i in range(len(s)):
        count[s[i]] += 1

    res = 0
    for i in range(len(s)):
        if check():
            break
        else:
            if count[s[i]] > 1:
                count[s[i]] -= 1
            res += 1
    print(res)
