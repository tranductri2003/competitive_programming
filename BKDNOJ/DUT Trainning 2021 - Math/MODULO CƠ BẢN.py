



A,B,C,M=list(map(int,input().split()))

AmuBmodM=pow(A,B,M)
nghichdao=pow(C,-1,M)

ans=(AmuBmodM*nghichdao)%M

print(ans)



