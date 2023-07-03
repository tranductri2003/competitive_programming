def findMissIT(lines):
    # Write your code here
    score = defaultdict(lambda: 0)
    time1 = defaultdict(lambda: 0)
    time2 = defaultdict(lambda: 0)
    for line in lines:
        line = list(map(int, line.split()))
        for i in range(1, 4):
            score[line[i]] += 4-i
            if 4-line[0] == 1:
                time1[line[i]] += 1
            elif 4-line[0] == 2:
                time2[line[i]] += 1

    temp = max(score.values())
    res = []
    for num in score.keys():
        if score[num] == temp:
            res.append(num)

    data1 = []
    data2 = []
    for num in res:
        data1.append(time1[num])
        data2.append(time2[num])

    res1 = []
    for num in res:
        if time1[num] == max(data1):
            res1.append(num)

    res2 = []
    for num in res1:
        if time2[num] == max(data2):
            res2.append(num)

    return (res2)