s1, s2 = input().split()
if len(s1) == len(s2):
    for i in range(len(s1)):
        if s1[i] < s2[i]:
            print(f"{s1}<{s2}")
            break
        elif s1[i] > s2[i]:
            print(f"{s1}>{s2}")
            break
    else:
        print(f"{s1}={s2}")
elif len(s1) < len(s2):
    for i in range(len(s1)):
        if s1[i] < s2[i]:
            print(f"{s1}<{s2}")
            break
        elif s1[i] > s2[i]:
            print(f"{s1}>{s2}")
            break
    else:
        print(f"{s1}<{s2}")
else:
    for i in range(len(s2)):
        if s1[i] < s2[i]:
            print(f"{s1}<{s2}")
            break
        elif s1[i] > s2[i]:
            print(f"{s1}>{s2}")
            break
    else:
        print(f"{s1}>{s2}")
