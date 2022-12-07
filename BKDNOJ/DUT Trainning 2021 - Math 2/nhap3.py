def prefixSum(test_list):
    res = [sum(test_list[ : i + 1]) for i in range(len(test_list))]
    return res

a=[1,2,3,4,5]
b=prefixSum(a)
print(b)