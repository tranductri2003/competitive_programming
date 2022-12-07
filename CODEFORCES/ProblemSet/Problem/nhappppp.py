
#?		 /\_/\
#?		(= ._.)
#?		/ >WA \>AC
#//     WELCOME TO MY CODING SPACE
#!      Filename: Palindrome dài nhất using hash VNOI.py
#*      Folder: D:\Code\Python\Codeforces\ProblemSet
#?      Author: TranDucTri2003
#TODO   CreatedAt: 2022-05-04 01:40:35

from operator import le


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
        hash_subString=self.Hash(subString)

        num=0
        l=len(string)
        length=l
        hash_string=self.Hash(string)
        hash_subString=self.Hash(subString)
        while length>1:
            for i in range(0,l-length+1):
                sub=self.getHash(i,i+length,hash_subString)
                

            
h=Hash()

"""
Cho xâu S.

Tìm độ dài của xâu con (liên tiếp) đối xứng dài nhất.
"""
n=int(input())
s=input()
dao=s[::-1]

