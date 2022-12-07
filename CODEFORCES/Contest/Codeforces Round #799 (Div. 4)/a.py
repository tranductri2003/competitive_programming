n = int(input())
souoc = 0
tonguoc = 0
for i in range(1, n+1):
    if i**2 > n:
        break
    if i**2 == n:
        souoc += 1
        tonguoc+=i
        break
    if n % i == 0:
        souoc += 2
        tonguoc+=i
        tonguoc+=n//i
print(souoc,tonguoc)
# 50
# 1 2 5      (7.07)   10 25 50


# 36
# 1 2 3 4      6      9 12 18 36
