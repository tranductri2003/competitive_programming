

import sys
from tabnanny import check
import time
import os
from io import BytesIO, IOBase
import math
from random import randint
from itertools import compress
from tkinter.tix import Tree
from webbrowser import get

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
 
def inputf(): 
    return sys.stdin.readline().rstrip("\r\n")  
 

 
def get_ints(): 
    return list(map(int, inputf().split()))
 
 
def get_string(): 
    return list(map(str, inputf().split()))




global maximum
 
 
def _lis(arr, n):
 

    global maximum
 

    if n == 1:
        return 1
 

    maxEndingHere = 1
 
    """Recursively get all LIS ending with arr[0], arr[1]..arr[n-2]
       IF arr[n-1] is maller than arr[n-1], and max ending with
       arr[n-1] needs to be updated, then update it"""
    for i in range(1, n):
        res = _lis(arr, i)
        if arr[i-1] < arr[n-1] and res+1 > maxEndingHere:
            maxEndingHere = res + 1
 

    maximum = max(maximum, maxEndingHere)
 
    return maxEndingHere
 
 
def LIS(arr):
 
    global maximum
 

    n = len(arr)
 

    maximum = 1
 

    _lis(arr, n)
 
    return maximum
 


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




def rwh_primes1v1(n):
    """ Returns  a list of primes < n for n > 2 """
    sieve = bytearray([True]) * (n//2)
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = bytearray((n-i*i-1)//(2*i)+1)
    return [2,*compress(range(3,n,2), sieve[1:])]

def rwh_primes1v2(n):
    """ Returns a list of primes < n for n > 2 """
    sieve = bytearray([True]) * (n//2+1)
    for i in range(1,int(n**0.5)//2+1):
        if sieve[i]:
            sieve[2*i*(i+1)::2*i+1] = bytearray((n//2-2*i*(i+1))//(2*i+1)+1)
    return [2,*compress(range(3,n,2), sieve[1:])]

sieveofE=[]
def SieveOfEratosthenes(n):
        
	prime = [True for i in range(n+1)]
	p = 2
	while (p * p <= n):


		if (prime[p] == True):


			for i in range(p * p, n+1, p):
				prime[i] = False
		p += 1

	for p in range(2, n+1):
		if prime[p]:
			sieveofE.append(p)


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


def maxSubArraySum(a,size):
     
    max_so_far = a[0]   
    max_ending_here = 0  
     
    for i in range(0, size):
        max_ending_here = max_ending_here + a[i]
        if max_ending_here < 0:
            max_ending_here = 0

        elif (max_so_far < max_ending_here):   
            max_so_far = max_ending_here
             
    return max_so_far

    



def lcm(x, y):


   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm


def primeFactors(n):
    a=[]

    while n % 2 == 0:
        a.append(2)
        n = n / 2
         

    for i in range(3,int(math.sqrt(n))+1,2):
         

        while n % i== 0:
            a.append(i)
            n = n / i

    if n > 2:
        a.append(n)
         

def findClosest(arr, n, target):
 

    if (target <= arr[0]):
        return arr[0]
    if (target >= arr[n - 1]):
        return arr[n - 1]
 

    i = 0; j = n; mid = 0
    while (i < j):
        mid = (i + j) // 2
 
        if (arr[mid] == target):
            return arr[mid]
 

        if (target < arr[mid]) :
 

            if (mid > 0 and target > arr[mid - 1]):
                return getClosest(arr[mid - 1], arr[mid], target)
 

            j = mid
         

        else :
            if (mid < n - 1 and target < arr[mid + 1]):
                return getClosest(arr[mid], arr[mid + 1], target)
                 

            i = mid + 1
         

    return arr[mid]
 
 

def getClosest(val1, val2, target):
 
    if (target - val1 >= val2 - target):
        return val2
    else:
        return val1

import random
 
def is_Prime(n):
    """
    Miller-Rabin primality test.
 
    A return value of False means n is certainly not prime. A return value of
    True means n is very likely a prime.
    """
    if n!=int(n):
        return False
    n=int(n)

    if n==0 or n==1 or n==4 or n==6 or n==8 or n==9:
        return False
 
    if n==2 or n==3 or n==5 or n==7:
        return True
    s = 0
    d = n-1
    while d%2==0:
        d>>=1
        s+=1
    assert(2**s * d == n-1)
 
    def trial_composite(a):
        if pow(a, d, n) == 1:
            return False
        for i in range(s):
            if pow(a, 2**i * d, n) == n-1:
                return False
        return True  
 
    for i in range(8):
        a = random.randrange(2, n)
        if trial_composite(a):
            return False
 
    return True  

def lcs(s1 , s2):
   m, n = len(s1), len(s2)
   prev, cur = [0]*(n+1), [0]*(n+1)
   for i in range(1, m+1):
       for j in range(1, n+1):
           if s1[i-1] == s2[j-1]:
               cur[j] = 1 + prev[j-1]
           else:
               if cur[j-1] > prev[j]:
                   cur[j] = cur[j-1]
               else:
                   cur[j] = prev[j]
       cur, prev = prev, cur
   return prev[n]
  
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
sys.stdout=open('output.txt','w')
sys.stdin=open('input.txt','r')
testcase=int(input())
for test in range(testcase):
    string=input()
    dodai=len(string)
    l=0
    #Kiem tra duoi 10
    check10=0
    currentMax=0
    for i in range(0,dodai-1):
        if int(string[i])+int(string[i+1])>=10:
            check10=1
            break
    if check10==1:
        pos=0
        for i in range(dodai-1,0,-1):
            if int(string[i])+int(string[i-1])>=10:
                pos=i-1
                break
        for i in range(0,pos+1):
            if i!=pos:
                print(string[i],end="")
            else:
                print(str(int(string[i])+int(string[i+1])),end="")
        for i in range(pos+2,dodai+1):
            if i==dodai:
                print(" ")
                break
            print(string[i],end="")
    else:
        print(str(int(string[0])+int(string[1])),end="")
        for i in range(2,dodai+1):
            if i==dodai:
                print(" ")
                break
            print(string[i],end="")

        
            
        
            
        

    
            