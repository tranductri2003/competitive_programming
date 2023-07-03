#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'findMissIT' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY lines as parameter.
#

from collections import defaultdict


def findMissIT(lines):
    # Write your code here
    score = defaultdict(lambda: 0)
    time1 = defaultdict(lambda: 0)
    time2 = defaultdict(lambda: 0)
    for line in lines:
        line = list(map(int, line.split()))
        for i in range(1, min(len(line), 4)):
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
    res2.sort()
    for i in range(len(res2)):
        res2[i] = str(res2[i])
    ans = " ".join(res2)
    return (ans)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    lines_count = int(input().strip())

    lines = []

    for _ in range(lines_count):
        lines_item = input()
        lines.append(lines_item)

    result = findMissIT(lines)
    fptr.write(result)

    fptr.close()
