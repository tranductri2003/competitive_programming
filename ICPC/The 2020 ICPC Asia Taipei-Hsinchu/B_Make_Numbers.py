# The problem can be solved by brute force as the flowing steps:
# Step 1. Enumerate all permutations of digits.
# Step 2. Enumerate all possible position subsets for inserting operations to the digit se-
# quence.
# Step 3. Enumerate all possible arithmetic expressions.
# Step 4. Evaluate all possible expressions and count the number of distinct result values.
# Step 5. Output the number.
# Complexity
# The maximum number of possible expressions is equal to 4! x (C x 3+C × 32 +C} × 3³)
#  = 1512. 

from itertools import permutations

a,b,c,d=list(map(str,input().split()))

result=[]
data=list(permutations([a,b,c,d]))

for num in data:
    #TH1: Bo dau vao 1 trong 3 khoang trong
    for i in range(1,4):
        so1=num[:i]
        so2=num[i:]
        so1=int("".join(so1))
        so2=int("".join(so2))
        # print(f"so1 la {so1}, so2 la {so2}")       
        operations=["+","-","*"]
        for j in operations:
            if j=="+":
                result.append(so1+so2)
            elif j=="*":
                result.append(so1*so2)
            else:
                result.append(so1-so2)
    #TH2: Bo dau vao 2 trong 3 khoang trong
    for i in range(1,3):
        for j in range(i+1,4):
            so1=num[:i]
            so2=num[i:j]
            so3=num[j:]
            so1=str("".join(so1))
            so2=str("".join(so2))  
            so3=str("".join(so3))
            for dau1 in operations:
                for dau2 in operations:
                    equation=str(so1+dau1+so2+dau2+so3)
                    # print(equation)
                    result.append(eval(equation))
    #TH3: Bo dau vao 3 trong 3 khoang trong
    so1=num[0]
    so2=num[1]
    so3=num[2]
    so4=num[3]
    so1=str("".join(so1))
    so2=str("".join(so2))  
    so3=str("".join(so3))
    so4=str("".join(so4))
    for dau1 in operations:
        for dau2 in operations:
            for dau3 in operations:
                equation=str(so1+dau1+so2+dau2+so3+dau3+so4)
                # print(equation)
                result.append(eval(equation))
    
    
                    
result=set(result) 
results=[]          
for num in result:
    if num>=0:
        results.append(num)

print(len(results))
                
    