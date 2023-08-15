from collections import defaultdict 
def compare_sublist(sublist):
    return tuple(sublist)

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    result = -1  # Giá trị mặc định nếu không tìm thấy

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] <= target:
            # Cập nhật kết quả và tiếp tục tìm kiếm phía bên phải
            result = arr[mid]
            left = mid + 1
        else:
            # Tìm kiếm phía bên trái
            right = mid - 1

    return result
t=int(input())
for _ in range(t):
    n=int(input())
    data=[]
    for i in range(n):
        temp = list(map(int,input().split()))
        data.append(temp)
    q=int(input())
    option = list(map(int,input().split()))
    data.sort(key=compare_sublist)
    i=0
    
    
    dichden = defaultdict(lambda:0)
    while i<n:
        j=i
        while j<n and data[i][3]>=data[j][0]:
            dichden[data[i][0]]=data[j][3]
            j+=1
        i=j
    dulieu=[]            
    for num in dichden:
        dulieu.append(num)
    res=[]
    for num in option:
        temp = binary_search(dulieu, num)
        res.append(max(dichden[temp],num))
    print(*res)