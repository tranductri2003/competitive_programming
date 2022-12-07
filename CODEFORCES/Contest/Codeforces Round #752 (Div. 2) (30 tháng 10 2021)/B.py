 
# global variable to store the maximum
global maximum
 
 
def _lis(arr, n):
 
    # to allow the access of global variable
    global maximum
 
    # Base Case
    if n == 1:
        return 1
 
    # maxEndingHere is the length of LIS ending with arr[n-1]
    maxEndingHere = 1
 
    """Recursively get all LIS ending with arr[0], arr[1]..arr[n-2]
       IF arr[n-1] is maller than arr[n-1], and max ending with
       arr[n-1] needs to be updated, then update it"""
    for i in range(1, n):
        res = _lis(arr, i)
        if arr[i-1] < arr[n-1] and res+1 > maxEndingHere:
            maxEndingHere = res + 1
 
    # Compare maxEndingHere with overall maximum. And
    # update the overall maximum if needed
    maximum = max(maximum, maxEndingHere)
 
    return maxEndingHere
 
 
def lis(arr):
 
    # to allow the access of global variable
    global maximum
 
    # length of arr
    n = len(arr)
 
    # maximum variable holds the result
    maximum = 1
 
    # The function _lis() stores its result in maximum
    _lis(arr, n)
 
    return maximum
 






testcase=int(input())

for test in range(0,testcase):
    n=int(input())
    a=list(map(int,input().split()))

    if n%2==0:
        print("YES")
    else:
        for i in range(0,n-1):
            if a[i]>=a[i+1]:
                print("YES")
                break
        else:
            print("NO")