
# while True:
#     print("?", 1, 2, flush=True)
#     t = int(input())
#     if t == 0:
#         quit()
#     data.append(t)
#     data = list(set(data))
#     if len(data) == 2:
#         stop = True
#         break
#     count += 1
#     if count == 50:
#         break

# if count >= 50 and stop == False:
#     print("!", data[0]*2, flush=True)
# else:
#     print("!", sum(data), flush=True)

stop = False
n = -1
check = [-1]*51
for i in range(2, 51):
    print("?", 1, i)
    t1 = int(input())
    if t1 == -1:
        n = i-1
        stop = True
        break
    print("?", i, 1)
    t2 = int(input())
    if t1 == t2:
        pass
    else:
        break

if stop == True:
    print(n)
else:
    print("!", t1+t2)
