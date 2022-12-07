
#?		 /\_/\
#?		(= ._.)
#?		/ >WA \>AC
#//     WELCOME TO MY CODING SPACE
#!      Filename: Xâu con using hash VNOI.py
#*      Folder: D:\Code\Python\Codeforces\ProblemSet
#?      Author: TranDucTri2003
#TODO   CreatedAt: 2022-05-03 23:01:47


MOD=10**9+7
base=31

pow=[0]*10**6
pow[0]=1



for i in range(1,10**6):
    pow[i]=pow[i-1]*base%MOD

def Hash(s):
    hash=[0]*(len(s)+1)
    for i in range(1,len(s)+1):
        hash[i]=(hash[i-1]*base  +  ord(s[i-1])-97+1) % MOD
    return hash

def getHash(i,j,hash):
    return (hash[j] -  hash[i-1]*pow[j-i+1]) % MOD

stringT=input()
stringP=input()
hashT=Hash(stringT)
hashP=Hash(stringP)[-1]

#Fiding substrings of T equal to string P

for i in range(1,len(stringT)-len(stringP)+2):
    if hashP==getHash(i,i+len(stringP)-1,hashT):
        print(i,end=" ")

class Hash:
    def __init__(self):
        self.MOD=10**9+7
        self.base=31
        self.pow=[0]*10**6
        self.pow[0]=1
        for i in range(1,10**6):
            self.pow[i]=self.pow[i-1]*self.base%self.MOD
    def Hash(self,s):
        hash=[0]*(len(s)+1)
        for i in range(1,len(s)+1):
            hash[i]=(hash[i-1]*self.base  + ord(s[i-1])-97+1 ) % self.MOD
        return hash
    
    def getHash(self,i,j,hash):
        return (hash[j] -  hash[i-1]*self.pow[j-i+1]) % self.MOD
    
    def subOccurrences(self,string,subString):
        hash_string=self.Hash(string)
        hash_subString=self.Hash(subString)[-1]

        occurrences=[]
        for i in range(1,len(string)-len(subString)+2):
            if hash_subString==self.getHash(i,i+len(subString)-1,hash_string):
                occurrences.append(i)
        return occurrences
s=Hash()
# print(*s.subOccurrences(input(),input()))
