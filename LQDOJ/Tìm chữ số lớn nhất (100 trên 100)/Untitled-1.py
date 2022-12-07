# Binary Search

def binary_search(data, giatricantim):

    low = 0
    high = len(data) - 1

    while low <= high:

        middle = (low + high)//2

        if data[middle] == giatricantim:
            return middle
        elif data[middle] > giatricantim:
            high = middle - 1
        else:
            low = middle + 1

    return -1
    
data = [1,3,4,6,7,8,10,13,14,18,19,21,24,37,40,45,71]
giatricantim = 7

print(binary_search(data, giatricantim))