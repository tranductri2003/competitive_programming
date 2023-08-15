#!/usr/bin/python3

n = int(input())

expected = []

while len(expected) < n:
    line = list(map(int, input().split(' ')))
    expected += line

stack = [-1] * (n + 1)
top = 0

bestAmount = -1
bestStart = -1
bestEnd = -1

for w in range(n):
    # pop any larger values off the stack and check for best
    while top > 0 and expected[stack[top-1]] > expected[w]:
        top -= 1
        if top == 0:
            nWeeks = w
        else:
            nWeeks = w - stack[top-1] - 1
        # print("pop",top,stack[top],expected[stack[top]],nWeeks)
        if nWeeks * expected[stack[top]] > bestAmount:
            bestAmount = nWeeks * expected[stack[top]]
            if top == 0:
                bestStart = 0
            else:
                bestStart = stack[top-1] + 1
            bestEnd = w - 1

    # if this week's expected > highest-known previous (and valid!) value, push
    if top == 0 or expected[w] >= expected[stack[top - 1]]:
        stack[top] = w
        top += 1

# all done scanning weeks, now see if any remaining expected values are better
while top > 0:
    top -= 1
    if top == 0:
        nWeeks = n
    else:
        nWeeks = n - stack[top - 1] - 1
    #print("postpop", top, stack[top], expected[stack[top]], nWeeks)
    if nWeeks * expected[stack[top]] >= bestAmount:
        bestAmount = nWeeks * expected[stack[top]]
        if top == 0:
            bestStart = 0
        else:
            bestStart = stack[top - 1] + 1
        bestEnd = n - 1

print(bestStart+1, bestEnd+1, bestAmount)
