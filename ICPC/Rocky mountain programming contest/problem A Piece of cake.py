canh,ngang,doc=list(map(int,input().split()))


a=max(4*ngang*doc,4*(canh-ngang)*doc,4*ngang*(canh-doc),4*(canh-ngang)*(canh-doc))

print(a)