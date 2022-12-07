# You decided to delete vertices from the tree one by one.
# On each step you select such a non-root vertex that 
# it does not respect its parent and none of its children respects it.
# If there are several such vertices, you select the one with the smallest number.
# When you delete this vertex v, all children of v become connected with the parent of v.

# The next n lines describe the tree: the i-th line contains two integers pi and ci (1≤pi≤n, 0≤ci≤1), where pi is the parent of the vertex i,
# and ci=0, if the vertex i respects its parents, and ci=1, if the vertex i does not respect any of its parents. The root of the tree has −1 instead of the parent index, also, ci=0 for the root.
# It is guaranteed that the values pi define a rooted tree with n vertices.


from collections import defaultdict
n=int(input())

safe=defaultdict(lambda:False)
for i in range(1,n+1):
    a,b=list(map(int,input().split()))
    if b==0: #Respect
        safe[i]=True
        safe[a]=True

stop=True
for i in range(1,n+1):
    if safe[i]==False:
        print(i,end=" ")
        stop=False
if stop==True:
    print(-1)