
def upper_bound(my_list, key):
    large = len(my_list) -1
    small = 0

    while (small <= large):
        mid = (small + large) // 2
        if my_list[mid] < key:  #Đổi thành if my_list[mid] > key:  trong th mảng từ lớn đến bé 
            small = mid + 1
        elif my_list[mid] > key:  #Đổi thành elif my_list[mid] < key: trong th mảng từ lớn đến bé
            large = mid - 1
        else:
            return mid
    if my_list[mid]>key:
        return mid
    else:
        return mid+1   #Đổi thành mid-1 trong th mảng từ lớn đến bé
    


t=int(input())
for _ in range(t):
    n,q=list(map(int,input().split()))
    a=list(map(int,input().split()))
    a.sort(reverse=True)
    prefixSum=[0]
    temp=0
    for num in a:
        temp+=num
        prefixSum.append(temp)
    for i in range(q):
        u=int(input())
        pos=upper_bound(prefixSum,u)
        if pos>n:
            print(-1)
        else:
            print(pos)
        
    
    