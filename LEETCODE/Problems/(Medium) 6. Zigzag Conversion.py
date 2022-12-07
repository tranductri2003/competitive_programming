from collections import defaultdict

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        matrix=defaultdict(lambda: defaultdict(lambda: 0))
        # matrix=[]
        # for i in range(1000):
        #     matrix.append([])
        #     for j in range(1000):
        #         matrix[i].append(0)
        i=0
        r=0
        c=0

        while i<len(s):
            while r<numRows:
                if i==len(s):
                    break
                matrix[r][c]=s[i]
                i+=1
                r+=1
            r-=1

            while r!=1:
                r-=1
                c+=1
                if i==len(s):
                    break
                matrix[r][c]=s[i]
                i+=1
            r=0
            c+=1
        res=[]
        for i in range(numRows+2):
            for j in range(c):
                if matrix[i][j]!=0:
                    res.append(matrix[i][j])
        res="".join(res)
        return res

            
        

"""
from collections import defaultdict

class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1:
            return s
        matrix=defaultdict(lambda: defaultdict(lambda: 0))

        matrix=[]
        for i in range(numRows):
            matrix.append([])
            for j in range(len(s)):
                matrix[i].append(0)
        i=0
        r=0
        c=0

        while i<len(s):
            while r<numRows:
                if i==len(s):
                    break
                matrix[r][c]=s[i]
                i+=1
                r+=1
            r-=1

            while r!=1:
                r-=1
                c+=1
                if i==len(s):
                    break
                matrix[r][c]=s[i]
                i+=1
            r=0
            c+=1
        res=[]
        for i in range(numRows):
            for j in range(c):
                try:
                    if matrix[i][j]!=0:
                        res.append(matrix[i][j])
                except(RuntimeError, IndexError): 
                    break

        res="".join(res)
        return res

            
        


t=Solution()
a="A"

n=2
t.convert(a, n)
"""
