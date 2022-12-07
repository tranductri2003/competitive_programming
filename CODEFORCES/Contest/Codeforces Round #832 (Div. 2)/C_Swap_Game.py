
# A Python program that takes in an array of integers and prints out the name of the person who wins
# the game.
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    if a[0] == min(a):
        print("Bob")
    else:
        print("Alice")
