from queue import PriorityQueue
from collections import deque,OrderedDict,defaultdict,Counter
from heapq import heappop, heappush, heapify
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


"""
 
"""
"""from collections import defaultdict

a={}
a=DefaultDict(lambda:0,a)
print(a[5])"""
# NOT MY CODE
# https://codeforces.com/contest/1324/submission/73179914
 
## PYRIVAL BOOTSTRAP
# https://github.com/cheran-senthil/PyRival/blob/master/pyrival/misc/bootstrap.py
# This decorator allows for recursion without actually doing recursion
from types import GeneratorType
 
def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    if not stack:
                        break
                    stack.pop()
                    to = stack[-1].send(to)
            return  to
 
    return wrappedfunc


# generic memoizer
def memoize(func):
    '''Memoizing decorator that checks whether the wrapped function 
    has been previously run with the current argument value. 
    If it has then that value is retrieved and offered instead 
    of rerunning the function'''
    memos = {}
    def wrapper(x):
        if x not in memos:
            memos[x] = func(x)
        return memos[x]
    return wrapper
from collections import defaultdict
from heapq import heappop, heappush

class Graph:
    INF=10**9
    #Searching Algorithms: DFS, BFS
    def __init__(self):
        self.graph = defaultdict(list)
        self.count=defaultdict(lambda:0)
    def addEdge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)  
        
        
    # Algorithms for finding the shortest path: Bellman Ford
    # def __init__(self, vertices):
    #     self.V = vertices # No. of vertices
    #     self.graph = []
    # def addEdge(self, u, v, w):
    #     self.graph.append([u, v, w])
    
    
    # Algorithms for finding the shortest path: Dijsktra
    # def __init__(self,vertices):
    #     self.distance=[self.INF]*vertices
    #     self.edges=defaultdict(dict)
    # def addEdge(self,u,v,w):
    #     self.edges[u][v]=w
    
    
    # Algorithms for finding the shortest path: Floyd Warshall    
    # def __init__(self,vertices):
    #     self.distance=defaultdict(lambda:defaultdict(lambda:self.INF))
    #     self.edges=defaultdict(lambda:defaultdict(lambda:self.INF))
    #     for i in range(1,vertices+1):
    #         self.distance[i][i]=0
    #         self.edges[i][i]=0
    # def addEdge(self,u,v,w):
    #     self.edges[u][v]=w
    
    
    #Minimum Spanning Trees: Kruskal's Algorithm
    # def __init__(self, vertices):
    #     self.vertices=vertices
    #     self.graph=[]
    # def addEdge(self,node1,node2,weight):
    #     self.graph.append([node1,node2,weight])


    # Ford-Fulkerson Algorithm for Maximum Flow Problem
    # def __init__(self):
    #     self.edges=defaultdict(lambda:defaultdict(lambda:0))
    # def addEdge(self,u,v,w):
    #     self.edges[u][v]=w            
    
    #Bipatite graph
    # def __init__(self):
    #     self.graph=defaultdict(list)  
    # def addEdge(self,u,v):
    #     self.graph[u].append(v)
    #     self.graph[v].append(u)
    
        
    def DFSUtil(self, vertex,visited,path):
        stack=[vertex]
        while len(stack):
            u=stack.pop()
            if visited[u]==0:
                path.append(u)
                visited[u]=1
                for neighbour in self.graph[u]:
                    stack.append(neighbour)
    # 1.Handling A Disconnected Graph:                 
    def DFS(self,numVertex):
        visited=defaultdict(lambda:0)
        path=[]
        for vertex in range(1,numVertex+1):
            if visited[vertex]==0:
                self.DFSUtil(vertex,visited,path)        
        return path
                
    # 2.DFS from a vertex 
    # def DFS(self,vertex):
    #     path=[]
    #     stack=[vertex]
    #     visited=defaultdict(lambda:0)
    #     while len(stack):
    #         u=stack.pop()
    #         if visited[u]==0:
    #             path.append(u)
    #             visited[u]=1
    #             for neighbour in self.graph[u]:
    #                 stack.append(neighbour)
    #     return path
                

                
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
    #     path=[]
    #     queue=[vertex]
    #     visited=defaultdict(lambda:0)
    #     while len(queue):
    #         u=queue.pop(0)
    #         if visited[u]==0:
    #             path.append(u)
    #             visited[u]=1
    #             for neighbour in self.graph[u]:
    #                 queue.append(neighbour)
    #     return path
        
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
    
          
    def connectedComponentsDFS(self,numVertex):
        path=[]
        visited=defaultdict(lambda:0)
        for vertex in range(1,numVertex+1):
            if visited[vertex] == 0:
                temp = []
                path.append(self.DFSUtilConnect(temp, vertex, visited))
        return path
      
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
                  

    def BellmanFord(self, S):
        d=defaultdict(lambda:self.INF)
        trace=defaultdict(lambda:-1)
        d[S]=0
 
        for _ in range(self.V - 1):
            for u, v, w in self.graph:
                if d[u]!=self.INF and d[v]>d[u]+w:
                    d[v]=d[u]+w
                    trace[v]=u

        #Trả về đường đi từ đỉnh S đến u nào đó
        #return trace
        # if u!=S and trace[u]==-1:
        #     return -1 #Không có đường đi
        # else:
        #     path=[]
        #     while u!=-1:
        #         path.append(u)
        #         u=trace[u]
        #     path.reverse()
        #     return path

        #Nhận biết đường đi âm vô cực trong trường hợp có chu trình âm:
        
        # Chạy thuật toán Bellman-Ford thêm một lần nữa với N vòng lặp, những đỉnh nào vẫn còn tối ưu được ở lần chạy thứ hai
        # sẽ tối ưu được mãi mãi, và đó là các đỉnh không tồn tại đường đi ngắn nhất.
        
        for _ in range(self.V):
            for u, v, w in self.graph:
                if d[u]!=self.INF and d[v]>d[u]+w:
                    d[v]=-self.INF  # vẫn còn tối ưu được --> âm vô cực
                    trace[v]=u
        return d
    
    def Dijsktra(self,S):
        self.distance[S]=0
        queue=[(0,S)]
        trace=defaultdict(lambda:-1)
        while queue:
            cost,vertex=heappop(queue)
            for neighbour, weight in self.edges[vertex].items():
                if cost+weight<self.distance[neighbour]:
                    self.distance[neighbour]=cost+weight
                    heappush(queue, (cost + weight, neighbour))
                    trace[neighbour]=vertex
        #Trả về đường đi từ đỉnh S đến u nào đó
        #return trace
        # if u!=S and trace[u]==-1:
        #     return -1 #Không có đường đi
        # else:
        #     path=[]
        #     while u!=-1:
        #         path.append(u)
        #         u=trace[u]
        #     path.reverse()
        #     return path 
        return self.distance
    
    def FloydWarshall(self,vertices):
        for k in range(1,vertices+1):
            for i in range(1,vertices+1):
                for j in range(1,vertices+1):
                   self.distance[i][j]=min(self.distance[i][j],self.edges[i][k]+self.edges[k][j])
        return self.distance


    #Finds the root of a subtree containing node 'i'
    def findSubtree(self,parent,i):
        if parent[i]==i:
            return i
        else:
            return self.findSubtree(parent,parent[i])
    #Connects subtrees containing node 'x' and 'y'
    def connectSubtree(self,parent,subtreeSize,x,y):
        xroot=self.findSubtree(parent,x)
        yroot=self.findSubtree(parent,y)
        if subtreeSize[xroot]<subtreeSize[yroot]:
            parent[xroot]=yroot
        elif subtreeSize[xroot]>subtreeSize[yroot]:
            parent[yroot]=xroot
        else:
            parent[yroot]=xroot
            subtreeSize[xroot]+=1
        
    def Kruskal(self):
        #Resulting tree
        res=[]
        
        #Iterator
        i=0
        #Number of edges in MST
        e=0

        #Sort edges by their weight
        self.graph=sorted(self.graph,key=lambda item: item[2])

        #Auxiliary arrays
        parent=[]
        subtreeSize=[]
        
        #initialize parent and subtreeSize arrays
        
        for node in range(self.vertices):
            parent.append(node)
            subtreeSize.append(0)
        
        #Number of edges in a MST is (node-1)
        
        while e<self.vertices-1:
            node1,node2,weight=self.graph[i]
            i+=1

            x=self.findSubtree(parent,node1)
            y=self.findSubtree(parent,node2)
            
            if x!=y:
                e+=1
                res.append([node1,node2,weight])
                self.connectSubtree(parent,subtreeSize,node1,node2)
        return res




    #Ford-Fulkerson Algorithm for Maximum Flow Problem
        
    """
    Return true if there is a path from source 's' to
    residual graph. Also fills parent[] to store the path"""

    def BFS(self,s,t,parent):
        visited=defaultdict(lambda:False)
        queue=[]
        
        queue.append(s)
        visited[s]=True

        while queue:
            u=queue.pop(0)
            for v in list(self.edges[u]):
                if visited[v]==False and self.edges[u][v]>0:
                    queue.append(v)
                    visited[v]=True
                    parent[v]=u
                    if v==t:
                        return True
        return False

    #Returns the maximum flow from s to t in the given graph
    def FordFulkerson(self,source, sink):
        parent=defaultdict(lambda:-1)
        maxFlow=0

        #Augment the flow while there is path from source to sink
        while self.BFS(source, sink,parent):
            # Find the minimum residual capacity of the edges along 
            #the path filled by BFS. Or we can say find the maximum flow
            #through the path found.
            pathFlow=self.INF
            s=sink
            while (s!=source):
                pathFlow=min(pathFlow,self.edges[parent[s]][s])
                s=parent[s]
            
            #Add path flow to overall flow
            maxFlow+=pathFlow

            #Update residual capatities of the edges and
            #reversed edges along the path
            v=sink
            while (v!=source):
                u=parent[v]
                self.edges[u][v]-=pathFlow
                self.edges[v][u]+=pathFlow
                v=parent[v]
        return maxFlow
    
    
    
    
    def isEulerian(self):
        path=self.connectedComponentsBFS(self.v)
        for compo in path:
            odd=0
            for vertex in compo:
                if self.degree[vertex]%2==1:
                    odd+=1

        if odd == 0:
            return 2   # graph has a Euler cycle
        elif odd == 2:
            return 1  # graph has a Euler path
        elif odd > 2:
            return 0   # graph is not Euleria
            # '''If odd count is 2, then semi-eulerian.
            # If odd count is 0, then eulerian
            # If count is more than 2, then graph is not Eulerian
            # Note that odd count can never be 1 for undirected graph'''

    def numCycle(self,vertex):
        path=[]
        stack=[vertex]
        visited=defaultdict(lambda:0)
        ancestor=defaultdict(lambda:0)
        num=0
        while len(stack):
            u=stack.pop()
            if visited[u]==0:
                path.append(u)
                visited[u]=1
                for neighbour in self.graph[u]:
                    ancestor[neighbour]=u
                    if visited[neighbour]==1 and ancestor[u]!=neighbour:  #Nếu đỉnh hàng xóm đã được thăm và tổ tiên của u không phải là đỉnh hàng xóm chứng tỏ có thêm 1 cycle
                        num+=1
                    else:  #Nếu đỉnh đó chưa được thăm thì DFS như bình thường
                        stack.append(neighbour)
        return num

    def isBipartite(self,src):
        colorArr=defaultdict(lambda:-1)
        colorArr[src]=1
        queue=[]
        queue.append(src)
        while queue:
            u=queue.pop(0)
            if u in self.graph[u]:
                return False
            for v in self.graph[u]:
                if colorArr[v]==-1:
                    colorArr[v]=1-colorArr[u]
                    queue.append(v)
                elif colorArr[v]==colorArr[u]:
                    return False
        return True
    
    def MaximumBipartiteMatching(self,x,y):
        # Use init and addEdge FordFulkerson
        for i in range(x):
            self.addEdge(0,i+1,1)
        for i in range(y):
            self.addEdge(x+i+1,x+y+1,1)
        return self.FordFulkerson(0,x+y+1)
    def sizeOfsubTree(self,s,e):
        self.count[s]=1
        for u in self.graph[s]:
            if u!=e:
                self.sizeOfsubTree(u,s)
                self.count[s]+=self.count[u]      


t=int(input())
for _ in range(t):
    n=int(input())
    print(n)
    ans=[i for i in range(1,n+1)]
    print(*ans)
    i=0
    while i<n-1:
        ans[i],ans[-1]=ans[-1],ans[i]
        print(*ans)
        i+=1
        
        
        