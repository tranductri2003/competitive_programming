import sys
sys.stdin = open("Round1.in", "r")
t = int(input())

for _ in range(t):
    n = int(input())
    if n > 26:
        print("No")
    else:
        print("Yes")
