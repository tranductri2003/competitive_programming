from itertools import permutations
import random


n = 5

tri_question = [2, 4, 5, -1 , -1]

data =[]
temp = [i for i in range(1,n+1)]
data =   list(permutations(temp))



for i in range(len(data)):
    temp_ans = list(data[i])
    temp_ques = []
    
    for i in range(n):

        for j in range(i,n):
            if temp_ans[j]>temp_ans[i]:
                temp_ques.append(j+1)
                break
        else:
            temp_ques.append(-1)
    if temp_ans==[4,1,3,5,2]:
        print("ans", temp_ques)
    if temp_ques==tri_question:
        print("YES")
    else:
        print("NO")