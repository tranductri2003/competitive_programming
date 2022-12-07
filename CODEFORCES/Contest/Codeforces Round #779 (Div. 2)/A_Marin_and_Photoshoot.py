#Một bức ảnh nhóm được coi là đẹp nếu cứ một đoạn tiếp giáp của ít nhất 2 cosplayer,
# số nam không vượt quá số nữ (hiển nhiên).

# . The i-th cosplayer is male if si=0 and female if si=1.

t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    res=0
    pos=[]
    for i in range(n):
        if s[i]=='0':
            pos.append(i)
    for i in range(len(pos)-1):
        if pos[i+1]==pos[i]+1:
            res+=2
        elif pos[i+1]==pos[i]   +2:
            res+=1
        
    print(res)