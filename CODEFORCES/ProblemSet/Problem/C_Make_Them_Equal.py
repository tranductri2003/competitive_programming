"""Not divisible-> Change"""  
"""
If the whole string is equal to c then you don't need to make any operations.

In order to find if it is possible with exactly 1 operation, we can pass through every x and count all the letters c that are divisible by x. This takes O(|s|log|s|) time complexity.

If for some x all its multiples are c then the answer is 1 operation with that x.

If all the above conditions don't hold you can always make 2 operations and make all the elements equal.

One possible way is with x=|s| and x=|s|−1.

After the first operation only the last element of s is not c thus if we use x=|s|−1 since gcd(|s|,|s|−1)=1 then |s| is not divisible by |s|−1 and it will become equal to c.

Time complexity: O(|s|log|s|) per test case.
"""  
import math
from collections import defaultdict

testcase=int(input())

for test in range(testcase):
    n,c=input().split()
    n=int(n)
    string=input()
    data=[]
    for i in range(0,n):
        if string[i]!=c:
            data.append(i+1)
    if data==[]:
        print(0)
    else:
        # !TLE
        # for i in range(2,n+1):
        #     for num in data:
        #         if num%i==0:
        #             break
        #     else:
        #         print(1)
        #         print(i)
        #         break
        # else:
        #     print(2)
        #     print(n,n-1)
        check=defaultdict(lambda:0)
        for num in data:
            for i in range(1,int(math.sqrt(num))+1):
                if num%i==0:
                    check[i]=1
                    check[num//i]=1
        for i in range(1,n+1):
            if check[i]==0:
                print(1)
                print(i)
                break
        else:
            print(2)
            print(n,n-1)
            
                    
                
                
                
                    
                    