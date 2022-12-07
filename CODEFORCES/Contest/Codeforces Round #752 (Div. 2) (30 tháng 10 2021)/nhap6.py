import sys
import time
import os
from io import BytesIO, IOBase

M=10**9+7
BUFSIZE = 8192
class FastIO(IOBase):
    newlines = 0
 
    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None
 
    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()
 
    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()
 
    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)
 
 
class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")
 
 
def print(*args, **kwargs):
    """Prints the values to a stream, or to sys.stdout by default."""
    sep, file = kwargs.pop("sep", " "), kwargs.pop("file", sys.stdout)
    at_start = True
    for x in args:
        if not at_start:
            file.write(sep)
        file.write(str(x))
        at_start = False
    file.write(kwargs.pop("end", "\n"))
    if kwargs.pop("flush", False):
        file.flush()
 
 
if sys.version_info[0] < 3:
    sys.stdin, sys.stdout = FastIO(sys.stdin), FastIO(sys.stdout)
else:
    sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")
 
def inputf(): return sys.stdin.readline().rstrip("\r\n")  # for fast input
 
 
def printf(var): sys.stdout.write(str(var)+"\n")  # for fast output, always take string
 
 
def get_ints(): return list(map(int, inputf().split()))
 
 
def get_string(): return list(map(str, inputf().split()))



#Hàm trả về dãy con có tăng dần dài nhất


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
 
 
def LIS(arr):
 
    # to allow the access of global variable
    global maximum
 
    # length of arr
    n = len(arr)
 
    # maximum variable holds the result
    maximum = 1
 
    # The function _lis() stores its result in maximum
    _lis(arr, n)
 
    return maximum
 
# Binary Search trả về index của giá trị cần tìm

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

    return middle   

#Upper bound trả về index của phần từ lớn hơn giá trị đưa vào
def upper_bound(my_list, key):
    large = len(my_list) -1
    small = 0

    while (small <= large):
        mid = (small + large) // 2
        if my_list[mid] < key:
            small = mid + 1
        elif my_list[mid] > key:
            large = mid - 1
        else:
            return mid
    if my_list[mid]>key:
        return mid
    else:
        return mid+1

#Upper bound trả về index của phần từ nhỏ hơn giá trị đưa vào

def lower_bound(my_list, key):
    large = len(my_list) -1
    small = 0

    while (small <= large):
        mid = (small + large) // 2
        if my_list[mid] < key:
            small = mid + 1
        elif my_list[mid] > key:
            large = mid - 1
        else:
            return mid
    if my_list[mid]<key:
        return mid
    else:
        return mid-1

#Sàng Eratosthenes tìm các số nguyên tố từ 2-10**6 trong 0.4s

# Python program to print all
# primes smaller than or equal to
# n using Sieve of Eratosthenes


def SieveOfEratosthenes(n):

	# Create a boolean array
	# "prime[0..n]" and initialize
	# all entries it as true.
	# A value in prime[i] will
	# finally be false if i is
	# Not a prime, else true.
	prime = [True for i in range(n+1)]
	p = 2
	while (p * p <= n):

		# If prime[p] is not
		# changed, then it is a prime
		if (prime[p] == True):

			# Update all multiples of p
			for i in range(p * p, n+1, p):
				prime[i] = False
		p += 1

	# Print all prime numbers
	for p in range(2, n+1):
		if prime[p]:
			print (p)

# -----------------------------roman nhập một số tự nhiên trả về số la mã của nó
def roman_number(x):
    if x > 15999:
        return
    value = [5000, 4000, 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    symbol = ["F", "MF", "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    roman = ""
    i = 0
    while x > 0:
        div = x // value[i]
        x = x % value[i]
        while div:
            roman += symbol[i]
            div -= 1
        i += 1
    return roman

#Hàm trả về dãy con liền kề có tổng lớn nhất Largest Sum Contiguous Subarray
def maxSubArraySum(a,size):
     
    max_so_far = a[0]   #Largest Sum Contiguous Subarray tính tới hiện tại
    max_ending_here = 0  #Sum đang trong quá trình kiểm tra
     
    for i in range(0, size):
        max_ending_here = max_ending_here + a[i]
        if max_ending_here < 0:
            max_ending_here = 0
         
        # Do not compare for all elements. Compare only  
        # when  max_ending_here > 0
        elif (max_so_far < max_ending_here):   #Đã max-ending-here<0 thì không xét cái này nữa, chỉ xét khi max-ending-here >0
            max_so_far = max_ending_here
             
    return max_so_far

    
#Hàm prefixSum trả về một list. 

#res[i]: tổng từ phần từ đầu đến phần tử a[i]
#1+7+9=res[4]-res[1]
def prefixSum(test_list):
    res = [sum(test_list[ : i + 1]) for i in range(len(test_list))]
    return res

"""
def find_shortest_path(graph, start, end, path):
    path = path + [start]
    if start == end:
        return path
    if start not in graph:
        return None
    shortest = None
    for node in graph[start]:
        if node not in path:
            newpath = find_shortest_path(graph, node, end, path)
            if newpath:
                if not shortest or len(newpath) < len(shortest):
                    shortest = newpath
    return shortest
""" 

"""
def dfs(root,nodeVal,nodeConnection,visited):
    leftVal = nodeVal[root][0]
    rightVal = nodeVal[root][1]
    solution = []
    if nodeConnection[root]:
        visited.add(root)
        for i in nodeConnection[root]:
            if i not in visited:
                solution.append(dfs(i,nodeVal,nodeConnection,visited))
        leftMax = 0
        rightMax = 0
        for i in solution:
            l, r = i
            leftMax += max(abs(leftVal - l[0]) + l[1], abs(leftVal - r[0]) + r[1])
            rightMax += max(abs(rightVal - l[0]) + l[1], abs(rightVal - r[0]) + r[1])
        return ((leftVal, leftMax), (rightVal, rightMax))
    else:
        return ((leftVal, 0), (rightVal, 0))
 
"""
 
"""
def BFS(adj,src,dist,paths,n):
    visited=[False]*n
    dist[src]=0
    paths[0]=1
    q=[src]
    visited[src]=True
    while(q):
        p=q.pop(0)
        for j in adj[p]:
            if not visited[j]:
                q.append(j)
                visited[j]=True
            if dist[j]>dist[p]+1:
                dist[j] = dist[p]+1
                paths[j] = paths[p]
            elif dist[j]==dist[p]+1:
                paths[j] +=paths[p]
    return paths
 
"""
