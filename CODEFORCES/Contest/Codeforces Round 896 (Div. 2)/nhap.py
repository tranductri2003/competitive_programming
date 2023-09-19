ip = [6,9,69,96]
print("ip", ip)
sm = [255,255,224,0]
print("sm", sm)
na=[]
for i in range(4):
    na.append(ip[i]&sm[i])

print("na",na)
notsm = [0,0,31,255]
ba=[]
for i in range(4):
    ba.append(na[i]^notsm[i])
print("ba",ba)
    
    
