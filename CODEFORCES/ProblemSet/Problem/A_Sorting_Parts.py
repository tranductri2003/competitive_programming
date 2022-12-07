"""
For each test case of input data, output "YES" (without quotes), 
if the array may be not sorted in non-decreasing order,
output "NO" (without quotes) otherwise. You can output each letter in any case (uppercase or lowercase).
"""

t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    if a==sorted(a):
        print("NO")
    else:
        print("YES")
