import time
sang=[1]*(10**6+1)
sang[0]=False
sang[1]=False

a=time.time()
MAX=10**6+1
i=2
while i*i<MAX:
    if sang[i]==True:
        j=i*i
        while j<MAX:
            sang[j]=False
            j+=i
    i+=1
b=time.time()
print(b-a)