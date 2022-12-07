s=input()
n=len(s)
class SegmentTree:
    def __init__(self):
        self.optimal=[0]*(4*n)
        self.open=[0]*(4*n)
        self.close=[0]*(4*n)
    def buildTree(self,a):
        pass
        

        
# Với mỗi nút(ví dụ như nút id, quản lý đoạn [l,r]) chúng ta lưu ba biến nguyên:

# optimal: Là kết quả tối ưu trong đoạn [l,r].
# open: Số lượng dấu ( sau khi đã xóa hết các phần tử thuộc dãy ngoặc đúng độ dài optimal trong đoạn.
# close: Số lượng dấu ) sau khi đã xóa hết các phần tử thuộc dãy ngoặc đúng độ dài optimal trong đoạn.


for _ in range(int(input())):
    l,r=list(map(int,input().split()))
    