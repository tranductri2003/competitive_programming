 



def binary_search(data, elem):
    
    low = 0
    high = len(data) - 1
    while low <= high:
      
        middle = (low + high)//2
        if data[middle] == elem:
            return middle
            
        elif data[middle] > elem:
            high = middle - 1
        else:
            low = middle + 1
    if data[middle] != elem:
        return False

















a=0
b=2
acceptedlist=list()
acceptedlist.append(0)
while a<10**9:
    a=a+b
    b=b+1
    acceptedlist.append(a)
b=20
print(binary_search(acceptedlist,b))
