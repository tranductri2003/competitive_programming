"""
    The idea here is to build a segment tree. Each node stores the left and right
    endpoint of an interval and the sum of that interval. All of the leaves will store
    elements of the array and each internal node will store sum of leaves under it.
    Creating the tree takes O(n) time. Query and updates are both O(log n).
"""

#Segment tree node
from re import L


class Node:
    def __init__(self,start,end):
        self.start = start
        self.end = end
        self.total = 0
        self.max = 0
        self.min = 0
        self.left = None
        self.right = None

class SegmentTree:
    def __init__(self,mang,n):
        self.a=mang
        self.N=n
        self.INF_MIN=-10**10
        self.INF_MAX=10**9
        def buildTree(mang,l,r):
            
            #base case
            if l>r:
                return None
            
            #leaf node
            if l==r:
                n=Node(l,r)
                n.total=mang[l]
                n.max=mang[l]
                n.min=mang[l]
                return n
            
            mid = (l+r)//2

            root=Node(l,r)
            
            #Recursively build the SegmentTree
            root.left=buildTree(mang,l,mid)
            root.right=buildTree(mang,mid+1,r)
            
            #Total stores the sum of all the leaves under root
            #i.e. those elements lying between (start,end)
            root.total=root.left.total+root.right.total
            root.max=max(root.left.max,root.right.max)
            root.min=min(root.left.min,root.right.min)
            
            return root
        self.root=buildTree(mang,0,n-1)
    
    def updateNode(self,i,val):
        def updateVal(root,i,val):
            
            #Base case. The actual value will be updated in a leaf.
            #The total is them propogated upwards
            if root.start==root.end:
                root.total=val
                root.max=val
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
            root.total=root.left.total+root.right.total
            root.max=max(root.left.max,root.right.max)
            root.min=min(root.left.min,root.right.min)
            
            return root
        return updateVal(self.root,i,val)
    
    def updateRange(self,u,v,val):  #u,v là đoạn cần update; l,r là biến tạm
        #l=root.start
        #r=root.end
        def updateVal(root,u,v,val):
            if u>root.end or v<root.start:
                return
            
            #Base case. The actual value will be updated in a leaf.
            #The total is them propogated upwards
            if root.start==root.end:
                root.total+=val
                root.max+=val
                root.min+=val
                return root
            
            mid = (root.start+root.end)//2
            updateVal(root.left,u,mid,val)
            updateVal(root.right,mid+1,v,val)          
            
            #Propogate the changes after recursive call returns
            root.total=root.left.total+root.right.total
            root.max=max(root.left.max,root.right.max)
            root.min=min(root.left.min,root.right.min)
            
            return root
        return updateVal(self.root,u,v,val)
    
    def sumRange(self,i,j):
        def rangeSum(root,i,j):
            
            #If the range exactly matches the root, we already have the sum
            if root.start ==i and root.end==j:
                return root.total
            
            mid = (root.start+root.end)//2
            
            #If end of the range is less than the mid, the entire interval lies
            #in the left subtree
            if j<=mid:
                return rangeSum(root.left,i,j)
            
            #If start of the interval is greater than the mid, the entire interval lies
            #in the right subtree
            elif i>=mid+1:
                return rangeSum(root.right,i,j)
            
            #Otherwise, the interval is split. So we calculate the sum recursively,
            #by splitting the interval
            else:
                return rangeSum(root.left,i,mid)+rangeSum(root.right,mid+1,j)
            
        return rangeSum(self.root,i,j)
    
    def getMax(self,l,r):   #l,r là đoạn lấy giá trị lớn nhất
        def getValue(root,l,r):
            if l>root.end or r<root.start:
                #Đoạn cần cập nhật nằm ngoài khoảng phạm vi của NODE thì ta bỏ qua
                return self.INF_MIN
            if root.start==l and root.end==r:
                return root.max
            
            mid=(root.start+root.end)//2
            # if r<=mid:
            #     return getValue(root.left,l,r)
            # elif l>mid+1:
            #     return getValue(root.right,l,r)
            # else:
            return max(getValue(root.left,l,mid),getValue(root.right,mid+1,r))
        return getValue(self.root,l,r)
           
    def getMin(self,l,r):   
        def getValue(root,l,r):
            if l>root.end or r<root.start:
                return self.INF_MAX
            if root.start==l and root.end==r:
                return root.min
            
            mid=(root.start+root.end)//2
            # if r<=mid:
            #     return getValue(root.left,l,r)
            # elif l>mid+1:
            #     return getValue(root.right,l,r)
            # else:
            return min(getValue(root.left,l,mid),getValue(root.right,mid+1,r))
        return getValue(self.root,l,r)
n=int(input())
a=list(map(int,input().split()))

ST=SegmentTree(a,n)

# Loại 1 có dạng   : Nấu gói mì ở vị trí thứ  và mua gói mì có độ ngon  thay vào đó. ()
# Loại 2 có dạng   : In ra độ ngon lớn nhất của các gói mì từ vị trí  đến  ()

# 1 4 2 3 5
# 3 4 2 3 5
# 3 3 2 3 5

import random


for _ in range(int(input())):
    t,l,r=list(map(int,input().split()))
    t=
    if t==1:
        ST.updateNode(l-1,r)
        a[l-1]=r

    else:
        if l==r:
            print(a[l-1])
        else:
            print(ST.getMax(l-1,r-1))
        