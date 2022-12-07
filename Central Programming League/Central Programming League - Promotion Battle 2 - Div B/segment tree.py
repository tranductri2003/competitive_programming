


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
        
      
            
n,m=list(map(int,input().split()))
a=[0]*(n+1)
t=SegmentTree(a,n)
t.buildTree(1,1,n)
for i in range(m):
    u,v,val=list(map(int,input().split()))
    t.updateTree(1,1,n,u,v,val)
for i in range(int(input())):
    u,v=list(map(int,input().split()))
    print(t.getValue(1,1,n,u,v))