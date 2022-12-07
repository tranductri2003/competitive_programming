
def upper_bound(my_list, key):
    large = len(my_list) -1
    small = 0

    while (small <= large):
        mid = (small + large) // 2
        if my_list[mid] > key:
            small = mid + 1
        elif my_list[mid] < key:
            large = mid - 1
        else:
            return mid
    if my_list[mid]>key:
        return mid
    else:
        return mid-1



testcase=int(input())
for test in range(testcase):
    n,l,r=list(map(int,input().split()))
    a=list(map(int,input().split()))
    a.sort(reverse=True)  #Avoid counting twice times
    
    res=0
    A=0
    B=0
    
    #Find all pairs which has sum greater or equal to l
    for i in range(0,n-1):
        currentNum=a[i]
        correspondingNum=l-currentNum
        position=upper_bound(a,correspondingNum)
        if position!=-1:
            for j in range(position,n):
                if a[j]!=a[position]:
                    position=j-1
                    break
                if j==n-1 and a[j]==a[position]:
                    position=j
                    break
            if position>i:
                A+=position-i
    
    #Find all pairs which has sum greater than r
    for i in range(0,n-1):
        currentNum=a[i]
        correspondingNum=r+1-currentNum
        position=upper_bound(a,correspondingNum)
        if position!=-1:
            for j in range(position,n):
                if a[j]!=a[position]:
                    position=j-1
                    break
                if j==n-1 and a[j]==a[position]:
                    position=j
                    break
            if position>i:
                B+=position-i
    res=A-B
    print(res)

                
    