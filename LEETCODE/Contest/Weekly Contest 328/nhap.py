'''Python3 program to implement 2D Binary Indexed Tree

2D BIT is basically a BIT where each element is another BIT.
Updating by adding v on (x, y) means it's effect will be found
throughout the rectangle [(x, y), (max_x, max_y)],
and query for (x, y) gives you the result of the rectangle
[(0, 0), (x, y)], assuming the total rectangle is
[(0, 0), (max_x, max_y)]. So when you query and update on
this BIT,you have to be careful about how many times you are
subtracting a rectangle and adding it. Simple set union formula
works here.

So if you want to get the result of a specific rectangle
[(x1, y1), (x2, y2)], the following steps are necessary:

Query(x1,y1,x2,y2) = getSum(x2, y2)-getSum(x2, y1-1) -
					getSum(x1-1, y2)+getSum(x1-1, y1-1)

Here 'Query(x1,y1,x2,y2)' means the sum of elements enclosed
in the rectangle with bottom-left corner's co-ordinates
(x1, y1) and top-right corner's co-ordinates - (x2, y2)

Constraints -> x1<=x2 and y1<=y2

	/\
y |
	|	 --------(x2,y2)
	|	 | |
	|	 | |
	|	 | |
	|	 ---------
	| (x1,y1)
	|
	|___________________________
(0, 0)			 x-->

In this program we have assumed a square matrix. The
program can be easily extended to a rectangular one. '''

N = 3  # N-.max_x and max_y

# A structure to hold the queries


class Query:

    def __init__(self, x1, y1, x2, y2):

        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2


# A function to update the 2D BIT
def updateBIT(BIT, x, y, val):

    while x <= N:

        # This loop update all the 1D BIT inside the
        # array of 1D BIT = BIT[x]
        while y <= N:
            BIT[x][y] += val
            y += (y & -y)

        x += (x & -x)

    return


# A function to get sum from (0, 0) to (x, y)
def getSum(BIT, x, y):
    x = n-y

    sum = 0

    while x > 0:
        # This loop sum through all the 1D BIT
        # inside the array of 1D BIT = BIT[x]
        while y > 0:

            sum += BIT[x][y]
            y -= y & -y

        x -= x & -x

    return sum


# A function to create an auxiliary matrix
# from the given input matrix
def constructAux(mat, aux):
    # Initialise Auxiliary array to 0
    for i in range(N + 1):
        for j in range(N + 1):
            aux[i][j] = 0

    # Construct the Auxiliary Matrix
    for j in range(1, N + 1):
        for i in range(1, N + 1):
            aux[i][j] = mat[N - j][i - 1]

    return


# A function to construct a 2D BIT
def construct2DBIT(mat, BIT):
    # Create an auxiliary matrix
    aux = [None for i in range(N + 1)]
    for i in range(N + 1):

        aux[i] = [None for i in range(N + 1)]

    constructAux(mat, aux)

    # Initialise the BIT to 0
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            BIT[i][j] = 0

    for j in range(1, N + 1):

        for i in range(1, N + 1):

            # Creating a 2D-BIT using update function
            # everytime we/ encounter a value in the
            # input 2D-array
            v1 = getSum(BIT, i, j)
            v2 = getSum(BIT, i, j - 1)
            v3 = getSum(BIT, i - 1, j - 1)
            v4 = getSum(BIT, i - 1, j)

            # Assigning a value to a particular element
            # of 2D BIT
            updateBIT(BIT, i, j, aux[i][j] -
                      (v1 - v2 - v4 + v3))

    return


# A function to answer the queries
def answerQueries(q, m, BIT):

    for i in range(m):

        x1 = q[i].x1 + 1
        y1 = q[i].y1 + 1
        x2 = q[i].x2 + 1
        y2 = q[i].y2 + 1

        ans = getSum(BIT, x2, y2) - \
            getSum(BIT, x2, y1 - 1) - \
            getSum(BIT, x1 - 1, y2) + \
            getSum(BIT, x1 - 1, y1 - 1)

        print("Query (", q[i].x1, ", ", q[i].y1, ", ",
              q[i].x2, ", ", q[i].y2, ") = ", ans, sep="")

    return


# Driver Code
mat = [[0, 0, 0, 0],
       [0, 0, 0, 0],
       [0, 0, 0, 0],
       [0, 0, 0, 0]]

# Create a 2D Binary Indexed Tree
BIT = [None for i in range(N + 1)]
for i in range(N + 1):

    BIT[i] = [None for i in range(N + 1)]
    for j in range(N + 1):
        BIT[i][j] = 0


construct2DBIT(mat, BIT)

''' Queries of the form - x1, y1, x2, y2
	For example the query- {1, 1, 3, 2} means the sub-matrix-
		y
		/\
	3 | 1 2 3 4	 Sub-matrix
	2 | 5 3 8 1	 {1,1,3,2} --.	 3 8 1
	1 | 4 6 7 5								 6 7 5
	0 | 2 4 8 9
		|
  ----- 0 1 2 3 ---. x
		|
	
		Hence sum of the sub-matrix = 3+8+1+6+7+5 = 30
	
	'''
q = [Query(2, 2, 3, 3), Query(0, 0, 1, 1)]
updateBIT(BIT, 3, 3, 2)
updateBIT(BIT, 1, 1, 1)
updateBIT(BIT, 2, 2, 1)

m = len(q)

answerQueries(q, m, BIT)

# This code is contributed by phasing17
