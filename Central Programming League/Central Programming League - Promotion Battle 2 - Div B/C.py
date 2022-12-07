
key=input()
a=input()

key=int(key,16)
key=bin(key)[2:]


a=int(a,16)
a=bin(a)[2:]

class Hash:
    def __init__(self):
        self.MOD=10**9+7
        self.base=31
        self.pow=[0]*10**5
        self.pow[0]=1
        for i in range(1,10**5):
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

        occurrences=0
        for i in range(1,len(string)-len(subString)+2):
            if hash_subString==self.getHash(i,i+len(subString)-1,hash_string):
                occurrences+=1
        return occurrences
g=Hash()
print(g.subOccurrences(a,key))


