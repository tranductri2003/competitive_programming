
# Python3 code to find the number of
# nodes in the subtree of each node
N = 9
 
# variables used to store data globally
count1 = [0] * (N)
 
# Adjacency list representation of tree
adj = [[] for i in range(N)]
 
# Function to calculate no. of
# nodes in subtree
def numberOfNodes(s, e):
 
    count1[s] = 1
    for u in adj[s]:
         
        # Condition to omit reverse path
        # path from children to parent
        if u != e:
            
            # recursive call for DFS
            numberOfNodes(u, s)
            
            # update count[] value of parent
            # using its children
            count1[s] += count1[u]
 
# Function to add edges in graph
def addEdge(a, b):
 
    adj[a].append(b)
    adj[b].append(a)
 
# Function to print result
def printNumberOfNodes():
 
    for i in range(1, N):
        print("Nodes in subtree of", i,
                        ":", count1[i])
 
# Driver Code
if __name__ == "__main__":

    # insertion of nodes in graph
    addEdge(1, 5)
    addEdge(3, 4)
    addEdge(3, 5)
    addEdge(2, 1)
    addEdge(2,6)
    addEdge(2, 7)
    addEdge(7,8)

     
    # call to perform dfs calculation
    # making 1 as root of tree
    numberOfNodes(2,0)
     
    # print result
    printNumberOfNodes()
     
# This code is contributed by Rituraj Jain


# Đầu tiên, lấy điểm 1 làm gốc và ghi lại rt "gốc" hiện tại. Khi truy vấn kích thước của cây con x,
# nếu rt nằm ngoài cây con x thì câu trả lời là size (x), ngược lại thì câu trả lời là n-size ( x ′),
# x ′ là con của x sẽ gặp khi đi lên từ rt.