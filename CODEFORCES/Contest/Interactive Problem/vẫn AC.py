l=1
r=10**6

while l<r:
    mid=(l+r+1)//2
    print(mid)
    a=input()
    if a==">=":
        l=mid
    else:
        r=mid-1
print(f"! {l}")
