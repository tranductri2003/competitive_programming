k1, k2 = list(map(int,input().split()))
l1 = (k1-0.5)*3
if l1-l1//1>=0.5:
    l1 = int(l1)+1
else:
    l1 = int(l1)
    
    
r1 = (k1+0.5)*3
if r1==int(r1):
    r1-=1
    r1 =int(r1)
else:
    r1 = int(r1)
    
    
l2 = (k2-0.5)*2
if l2-l2//1>=0.5:
    l2 = int(l2)+1
else:
    l2 = int(l2)



r2 = (k2+0.5)*2
if r2==int(r2):
    r2-=1
    r2 = int(r2)
else:
    r2 = int(r2)
    
def find_overlap(l1, r1, l2, r2):
    # Kiểm tra xem hai đoạn có giao nhau hay không
    if r1 < l2 or r2 < l1:
        return None  # Không có giao nhau
    else:
        # Tìm phần giao
        l = max(l1, l2)
        r = min(r1, r2)
        return (l, r)
    
if find_overlap(l1,r1,l2,r2)==None:
    print(0)
else:
    data=[]
    res = find_overlap(l1,r1,l2,r2)
    for i in range(res[0],res[1]+1):
        data.append(i)
    print(*data)