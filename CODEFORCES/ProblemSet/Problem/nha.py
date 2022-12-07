

class SegmentTree:
    def __init__(self,mang,n):
        self.a=mang
        self.N=n
        self.tree=[0]*(4*self.N)
        self.INF_MIN=-10**9
    
    def showTree(self):
        print(self.tree)
    
    def buildTree(self,id,l,r):  
        #Chú ý khi khởi tạo t.buildTree(id,l,r), id luôn phải bằng 1
        #l=0, r=n-1 hoặc ta phải thêm một phần tử bất kỳ vào đẩu mảng a rồi l=1, r=n

        if l==r:
            self.tree[id]=self.a[l];
            return
        m=(l+r)//2;
        self.buildTree(id*2,l,m)
        self.buildTree(id*2+1,m+1,r)
        
        self.tree[id]=max(self.tree[id*2],self.tree[id*2+1])
    
    def updateTree(self, id, l, r, u, v, val):  #u,v là đoạn cần cập nhật
        if u>r or v<l:
            return 
        if l==r:
            self.tree[id]+=val
            return
        m=(l+r)//2
        self.updateTree(id*2,l,m,u,v,val)
        self.updateTree(id*2+1,m+1,r,u,v,val)
        self.tree[id]=max(self.tree[id*2],self.tree[id*2+1])
        
    # def updateTree(self,id,l,r,i,v):
    #     if i<l or i>r:
    #         return 
    #     if l==r:
    #         self.tree[id]=i
    #         return 
    #     m=(l+r)//2
    #     self.updateTree(id*2,l,m,i,v)
    #     self.updateTree(id*2+1,m+1,r,i,v)

    #     self.tree[id]=max(self.tree[id*2],self.tree[id*2+1])
    
    
    def getValue(self,id,l,r,u,v):   #u,v là đoạn lấy giá trị lớn nhất
        if u>r or v<l:
        #Đoạn [u, v] không giao với đoạn [l, r], ta bỏ qua đoạn này
            return self.INF_MIN
        if l==r:
            return self.tree[id]
        m=(l+r)//2
        return max(self.getValue(id*2,l,m,u,v),self.getValue(id*2+1,m+1,r,u,v))
"""
    The idea here is to build a segment tree. Each node stores the left and right
    endpoint of an interval and the sum of that interval. All of the leaves will store
    elements of the array and each internal node will store sum of leaves under it.
    Creating the tree takes O(n) time. Query and updates are both O(log n).
"""

#Segment tree node
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
        self.INF_MIN=-10**9
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
    
    def update(self, i, val):
            """
            :type i: int
            :type val: int
            :rtype: int
            """
            #Helper function to update a value
            def updateVal(root, i, val):
                
                #Base case. The actual value will be updated in a leaf.
                #The total is then propogated upwards
                if root.start == root.end:
                    root.total = val
                    return val
            
                mid = (root.start + root.end) // 2
                
                #If the index is less than the mid, that leaf must be in the left subtree
                if i <= mid:
                    updateVal(root.left, i, val)
                    
                #Otherwise, the right subtree
                else:
                    updateVal(root.right, i, val)
                
                #Propogate the changes after recursive call returns
                root.total = root.left.total + root.right.total
                
                return root.total
            
            return updateVal(self.root, i, val)

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
    
mang=[1,2,3,4,5]
ST=SegmentTree(mang,5)
print(ST.sumRange(0,4))
ST.update(1,10)
print(ST.sumRange(1,2))


            
            


    
        