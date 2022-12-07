s=input()

for i in range(int (s)+1,10**9):
    if len(set(str(i)))==len(str(i)):
        print(i)
        break