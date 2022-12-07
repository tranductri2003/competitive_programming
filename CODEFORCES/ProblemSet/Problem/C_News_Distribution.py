from queue import PriorityQueue
from collections import deque
from collections import OrderedDict
from collections import defaultdict
import sys
import time
import os
from io import BytesIO, IOBase
import math
from random import randint
from itertools import compress

MOD=10**9+7
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
    return sys.stdin.readline().rstrip("\r\n")  # for fast input
 

 
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

def LCS(s1 , s2):
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

fib_matrix = [[1,1],
              [1,0]]

def matrix_square(A, mod):
    return mat_mult(A,A,mod)


def mat_mult(A,B, mod):
  if mod is not None:
    return [[(A[0][0]*B[0][0] + A[0][1]*B[1][0])%mod, (A[0][0]*B[0][1] + A[0][1]*B[1][1])%mod],
            [(A[1][0]*B[0][0] + A[1][1]*B[1][0])%mod, (A[1][0]*B[0][1] + A[1][1]*B[1][1])%mod]]


def matrix_pow(M, power, mod):
    if power <= 0:
      return M

    powers =  list(reversed([True if i=="1" else False for i in bin(power)[2:]])) #Order is 1,2,4,8,16,...

    matrices = [None for _ in powers]
    matrices[0] = M

    for i in range(1,len(powers)):
        matrices[i] = matrix_square(matrices[i-1], mod)


    result = None

    for matrix, power in zip(matrices, powers):
        if power:
            if result is None:
                result = matrix
            else:
                result = mat_mult(result, matrix, mod)

    return result
#print (matrix_pow(fib_matrix, n, 10**9+7)[0][1])


def multiply(T, M):
     
    a = (T[0][0] * M[0][0] + T[0][1] *
         M[1][0] + T[0][2] * M[2][0])            
    b = (T[0][0] * M[0][1] + T[0][1] *
         M[1][1] + T[0][2] * M[2][1])
    c = (T[0][0] * M[0][2] + T[0][1] *
         M[1][2] + T[0][2] * M[2][2])
    d = (T[1][0] * M[0][0] + T[1][1] *
         M[1][0] + T[1][2] * M[2][0])
    e = (T[1][0] * M[0][1] + T[1][1] *
         M[1][1] + T[1][2] * M[2][1])
    f = (T[1][0] * M[0][2] + T[1][1] *
         M[1][2] + T[1][2] * M[2][2])
    g = (T[2][0] * M[0][0] + T[2][1] *
         M[1][0] + T[2][2] * M[2][0])
    h = (T[2][0] * M[0][1] + T[2][1] *
         M[1][1] + T[2][2] * M[2][1])
    i = (T[2][0] * M[0][2] + T[2][1] *
         M[1][2] + T[2][2] * M[2][2])
             
    T[0][0] = a
    T[0][1] = b
    T[0][2] = c
    T[1][0] = d
    T[1][1] = e
    T[1][2] = f
    T[2][0] = g
    T[2][1] = h
    T[2][2] = i
 

def power(T, n):
 
    if (n == 0 or n == 1):
        return;
    M = [[ 1, 1, 1 ],
                [ 1, 0, 0 ],
                [ 0, 1, 0 ]]
 
    power(T, n // 2)
 
    multiply(T, T)
 
    if (n % 2):
        multiply(T, M)
 
def tribonacci(n):
     
    T = [[ 1, 1, 1 ],
        [1, 0, 0 ],
        [0, 1, 0 ]]
 
    if (n == 0 or n == 1):
        return 0
    else:
        power(T, n - 2)

    return T[0][0]

def check_colinear(x1,y1,x2,y2,x3,y3):
    doan12=math.sqrt((x1-x2)**2+(y1-y2)**2)
    doan13=math.sqrt((x1-x3)**2+(y1-y3)**2)
    doan23=math.sqrt((x2-x3)**2+(y2-y3)**2)
    if doan12==0 or doan13==0 or doan23==0:
        return False    
    else:
        cos12=(doan13**2+doan23**2-doan12**2)/(2*doan13*doan23)
        cos13=(doan12**2+doan23**2-doan13**2)/(2*doan12*doan23)
        cos23=(doan13**2+doan12**2-doan23**2)/(2*doan13*doan12)
        if cos12==-1 or cos12==1 or cos13==-1 or cos13==1 or cos23==-1 or cos23==1:
            return False
        else:
            return True
        

def check_quadrilateral(x1,y1,x2,y2,x3,y3,x4,y4):
    if check_colinear(x1,y1,x2,y2,x4,y4)==True and check_colinear(x1,y1,x2,y2,x3,y3)==True and check_colinear(x1,y1,x3,y3,x4,y4)==True and check_colinear(x2,y2,x3,y3,x4,y4)==True:
        return True
    else:
        return False


def linear_equation(x1,x2,y1,y2):
    if x1==x2: 
        return True
    if y1==y2:
        return False
    a=(y1-y2)/(x1-x2)
    b=y1-a*x1
    return a,b


def check_quadrilateral(x1,y1,x2,y2,x3,y3,x4,y4):
        check=0
        if linear_equation(x1,x2,y1,y2)==True: 
            if (x3>x1 and x4>x1) or (x3<x1 and x4<x1):
                check+=1
        elif linear_equation(x1,x2,y1,y2)==False: 
            if (y3>y1 and y4>y1) or (y3<y1 and y4<y1):
                check+=1
        else:
            a,b=linear_equation(x1,x2,y1,y2)
            if (a*x3+b-y3>0 and a*x4+b-y4>0) or (a*x3+b-y3<0 and a*x4+b-y4<0):
                check+=1
                
                
        if linear_equation(x2,x3,y2,y3)==True: 
            if (x4>x2 and x1>x2) or (x4<x2 and x1<x2):
                check+=1
        elif linear_equation(x2,x3,y2,y3)==False: 
            if (y4>y2 and y1>y2) or (y4<y2 and y1<y2):
                check+=1
        else:
            a,b=linear_equation(x2,x3,y2,y3)
            if (a*x4+b-y4>0 and a*x1+b-y1>0) or (a*x1+b-y1<0 and a*x4+b-y4<0):
                check+=1                               
                
                
        if linear_equation(x3,x4,y3,y4)==True: 
            if (x1>x3 and x2>x3) or (x1<x3 and x2<x3):
                check+=1
        elif linear_equation(x3,x4,y3,y4)==False: 
            if (y1>y3 and y2>y3) or (y1<y3 and y2<y3):
                check+=1
        else:
            a,b=linear_equation(x3,x4,y3,y4)
            if (a*x1+b-y1>0 and a*x2+b-y2>0) or (a*x1+b-y1<0 and a*x2+b-y2<0):
                check+=1               
                
                
        if linear_equation(x4,x1,y4,y1)==True: 
            if (x2>x1 and x3>x1) or (x2<x1 and x3<x1):
                check+=1
        elif linear_equation(x4,x1,y4,y1)==False: 
            if (y2>y1 and y3>y1) or (y2<y1 and y3<y1):
                check+=1
        else:
            a,b=linear_equation(x4,x1,y4,y1)
            if (a*x2+b-y2>0 and a*x3+b-y3>0) or (a*x2+b-y2<0 and a*x3+b-y3<0):
                check+=1                
        
        if check==4:
            return True
        else:
            return False

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
"""from collections import defaultdict

a={}
a=DefaultDict(lambda:0,a)
print(a[5])"""










from collections import defaultdict
 
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        
    def addEdge(self,u,v):
        self.graph[u].append(v)
        
    def DFSUtil(self, v,visited):
        visited[v]=1
        print(v,end=" ")
        for neighbour in self.graph[v]:
            if visited[neighbour]==0:
                self.DFSUtil(neighbour,visited)
                
    #DFSUtil in case finding Connected components
    def DFSUtilConnect(self, temp, v, visited):
        visited[v] = 1
        # Store the vertex to list
        temp.append(v)
        for neighbour in self.graph[v]:
            if visited[neighbour]==0:
                # Update the list
                temp = self.DFSUtilConnect(temp, neighbour, visited)
        return temp
    
    
    # 1.Handling A Disconnected Graph: 
    def DFS(self,numVertex):
        visited=defaultdict(lambda:0)
        for vertex in range(1,numVertex+1):
            if visited[vertex]==0:
                self.DFSUtil(vertex,visited)        
    # 2.DFS from a vertex 
    # def DFS(self,vertex):
    #     visited=defaultdict(lambda:0)
    #     self.DFSUtil(vertex,visited)
                
    # 1. Handling A Disconnected Graph:
    def BFS(self,numVertex):
        visited=defaultdict(lambda:0)
        queue=[]
        for i in range(1,numVertex+1):
            if visited[i]==0:
                queue.append(i)
                visited[i]=1
                while queue:
                    u=queue.pop(0)
                    print(u,end=' ')
                    for v in self.graph[u]:
                        if visited[v]==0:
                            queue.append(v)
                            visited[v]=1
    # 2. BFS from a vertex
    # def BFS(self,vertex):
    #     visited = defaultdict(lambda:0)
    #     queue=[]
    #     queue.append(vertex)
    #     visited[vertex]=1
    #     while queue:
    #         u=queue.pop(0)
    #         print(u,end=' ')
    #         for v in self.graph[u]:
    #             if visited[v]==0:
    #                 queue.append(v)
    #                 visited[v]=1
    def connectedComponentsBFS(self,numVertex):
        visited=defaultdict(lambda:0)
        stack=[]
        path=[]
        for i in range(1,numVertex+1):
            if visited[i]==0:
                stack.append(i)
                visited[i]=1
                temp=[]
                while stack:
                    u=stack.pop()
                    temp.append(u)
                    for v in self.graph[u]:
                        if visited[v]==0:
                            stack.append(v)
                            visited[v]=1
                path.append(temp)
        return path
                  
    
    def connectedComponentsDFS(self,numVertex):
        path=[]
        visited=defaultdict(lambda:0)
        for vertex in range(1,numVertex+1):
            if visited[vertex] == 0:
                temp = []
                path.append(self.DFSUtilConnect(temp, vertex, visited))
        return path
    
    

g=Graph()
n,m=list(map(int,input().split()))
for i in range(m):
    a=list(map(int,input().split()))
    num=a.pop(0)
    for j in range(num):
        if j==num-1:
            g.addEdge(a[-1],a[0])
        else:
            g.addEdge(a[j],a[j+1])
path=g.connectedComponentsBFS(n)
ketqua=[0]*(n+1)
for part in path:
    temp=len(part)
    for num in part:
        ketqua[num]=temp
print(*ketqua[1:])
