import sys
import random
from collections import defaultdict


def check(announce):
    if announce == "ACCESS GRANTED":
        quit()
    else:
        announce = list(announce.split())
        res = int((announce[2])[1:])
        return res


# Kiem tra do dai

currentString = ""

checkTime = defaultdict(lambda: 0)
for i in range(20):
    currentString += "a"
    print(currentString, flush=True)
    time = (check(input()))
    checkTime[len(currentString)] = time

value = max(checkTime.values())
for i in range(1, 21):
    if checkTime[i] == value:
        length = i
        break

currentString = "a"*length

currentString = list(currentString)
alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
currentTime = time


while True:
    for i in range(0, length):
        map = defaultdict(lambda: 0)
        for chu in alphabet:
            currentString[i] = chu
            print("".join(currentString), flush=True)
            time = check(input())
            map[chu] = time
        currentString[i] = (max(map))


chars = [chr(i) for i in list(range(ord('A'), ord('Z')+1)) +
         list(range(ord('a'), ord('z')+1))] + [str(i) for i in range(0, 10)]
random.shuffle(chars)


def interact():
    print(''.join(answer), flush=True)
    line = sys.stdin.readline().strip()
    if line == 'ACCESS GRANTED':
        sys.exit(0)
    return (int)(line[15:].split()[0])


for i in range(1, 21):
    answer = ['a' for _ in range(0, i)]
    if interact() > 5:
        break

for i in range(0, len(answer)):
    best = -1, ' '
    for c in chars:
        answer[i] = c
        timing = interact()
        if timing > best[0]:
            best = timing, c
    answer[i] = best[1]
