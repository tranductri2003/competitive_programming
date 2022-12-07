import time

n,k=list(map(int,input().split()))
#n: number of owners
#k: size of each team
prelist=[0]*n  #Preference list of each owner 
ownerlist=[0]*n #The final list of each owner

for i in range(0,n):    
    ownerlist[i]=list()
for i in range(0,n):
    prelist[i]=list(map(str,input().split()))
    prelist[i]=prelist[i][1:]
    
    
   
p=int(input())   #The total number of members
totallist={}  #The name of every member

for i in range(0,p):
    name=str(input())
    totallist[name]=0

res=0
#Tính thời gian tại thời điểm bắt đầu thuật toán
start_time = time.time()
while res<k:
    for i in range(0,n):
        if prelist[i]!=False:
            for name in prelist[i]:
                if totallist[name]==0:
                    ownerlist[i].append(name)
                    totallist[name]=1
                    break
            else:
                prelist[i]=False
        if prelist[i]==False:
            for name in totallist:
                if totallist[name]==0:
                    ownerlist[i].append(name)
                    totallist[name]=1
                    break
    res=res+1
for owner in ownerlist:
    for name in owner:
        print(name,end=" ")
    print(" ")

#Tính thời gian tại thời điểm kết thúc thuật toán
end_time = time.time()

#tính thời gian chạy của thuật toán Python
elapsed_time = end_time - start_time
print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")

