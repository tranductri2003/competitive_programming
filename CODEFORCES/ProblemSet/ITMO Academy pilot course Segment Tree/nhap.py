"""
    The idea here is to build a segment tree. Each node stores the left and right
    endpoint of an interval and the sum of that interval. All of the leaves will store
    elements of the array and each internal node will store sum of leaves under it.
    Creating the tree takes O(n) time. Query and updates are both O(log n).
"""

# We would like a data structure that can efficiently handle two types of operations:

# Update index $i$ to value $v$
# Report the minimum and the number of occurences of the minimum on a range $[l, r]$


# We can use a normal segment tree to handle range queries, but slightly modify each node and the merge operation. Let each node be a pair of values $(\texttt{val}, \texttt{cnt})$, where $\texttt{val}$ is the minimum value and $\texttt{cnt}$ is the number occurences of the minimum value.

# If node $c$ has two children $a$ and $b$, then

#If a.val < b.val, then c=a
#If a.val > b.val, then c=b
#If a.val == b.val, then c= (a.val,a.cnt+b.cnt)



#Segment tree node


class Node:
    def __init__(self,start,end):
        self.start = start
        self.end = end
        self.cnt=0
        self.min=0
        self.left = None
        self.right = None

class SegmentTree:
    def __init__(self,mang,n):
        self.a=mang
        self.N=n
        self.INF_MIN=-10**9
        self.INF_MAX=10**9
        def buildTree(mang,l,r):
            
            #base case
            if l>r:
                return None
            
            #leaf node
            if l==r:
                n=Node(l,r)
                n.min=mang[l]
                n.cnt=1
                return n
            
            mid = (l+r)//2

            root=Node(l,r)
            
            #Recursively build the SegmentTree
            root.left=buildTree(mang,l,mid)
            root.right=buildTree(mang,mid+1,r)
            
            #Total stores the sum of all the leaves under root
            #i.e. those elements lying between (start,end)

            
            if root.left.min < root.right.min:
                root.min=root.left.min
                root.cnt=root.left.cnt
            elif root.left.min > root.right.min:
                root.min=root.right.min
                root.cnt=root.right.cnt
            else:
                root.min=root.left.min
                root.cnt=root.left.cnt+root.right.cnt
            
            return root
        self.root=buildTree(mang,0,n-1)
    
    def updateNode(self,i,val):
        def updateVal(root,i,val):
            
            #Base case. The actual value will be updated in a leaf.
            #The total is them propogated upwards
            if root.start==root.end:
                root.min=val
                return root
            
            mid = (root.start+root.end)//2
            
            #If the index is less than the mid, that leaf must be in the left subtree
            if i<=mid:
                updateVal(root.left,i,val)
            #Otherwise, the right subtree
            else:
                updateVal(root.right,i,val)
            
            #Propogate the changes after recursive call returns
            if root.left.min < root.right.min:
                root.min=root.left.min
                root.cnt=root.left.cnt
            elif root.left.min > root.right.min:
                root.min=root.right.min
                root.cnt=root.right.cnt
            else:
                root.min=root.left.min
                root.cnt=root.left.cnt+root.right.cnt
            
            return root
        return updateVal(self.root,i,val)
           
    def getMin(self,l,r):   
        def getValue(root,l,r):
            # print(11,root.start,root.end)

            if root.end<l or root.start>r:
                return (self.INF_MAX,1)
            if root.start==root.end:
                return root.min, root.cnt           
            if root.start==l and root.end==r:
                # print('die',l,r,end=" ")
                # print(root.min,root.cnt)
                return root.min,root.cnt
            
            mid=(root.start+root.end)//2
            
            # print('buoc 1')
            minLeft,freLeft=getValue(root.left,l,r)
            # print(5555,minLeft)
            # print('buoc 2')
            minRight,freRight=getValue(root.right,l,r)
            # print(5555,minRight)
            # print("tinh xong thành phaafn")
            # print('trai',minLeft,'phai',minRight)

            if minLeft < minRight:
                root.min=minLeft
                root.cnt=freLeft
            elif minLeft > minRight:
                root.min=minRight
                root.cnt=freRight
            else:
                root.min=minLeft
                root.cnt=freLeft+freRight
            # print(22,root.min,root.cnt)
            return root.min,root.cnt

                
        return getValue(self.root,l,r)

n,q=list(map(int,input().split()))
a=list(map(int,input().split()))


ST=SegmentTree(a,n)
for _ in range(q):
    type,l,r=list(map(int,input().split()))
    if type==1:
        ST.updateNode(l,r)
    else:
        print(*ST.getMin(l,r-1))
        # print(*ST.getMin(l,l))



"""
    The idea here is to build a segment tree. Each node stores the left and right
    endpoint of an interval and the sum of that interval. All of the leaves will store
    elements of the array and each internal node will store sum of leaves under it.
    Creating the tree takes O(n) time. Query and updates are both O(log n).
"""

