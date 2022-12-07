listbangchucai=["a",	"b",	"c",	"d",	"e",	"f",	"g",	"h",	"i",	"j"	, "k",	"l",	"m",	"n",	"o",	"p",	"q",	"r",	"s",	"t",	"u",	"v",	"w","x"	,"y","z"]
listbiendich=list()
n=str(input())
i=0
while i<len(n):
    if n[i]=="9":
        listbiendich.append(listbangchucai[int(    int(n[i:i+2])-97    )]) 
        i=i+2
    elif n[i]=="1":
        listbiendich.append(listbangchucai[int(    int(n[i:i+3])-97    )]) 
        i=i+3

for num in listbiendich:
    print(num,end="")


if "0" not in n or sum%3!=0:
        print("-1")
else:
    chuoi=list(n)
    chuoi.sort(reverse=True)
    for i in range(0,len(chuoi)):
        max=max+int(int(chuoi[i])*10**(len(chuoi)-i-1))
        
    while max%30!=0:
        max=max-30

    print(max)