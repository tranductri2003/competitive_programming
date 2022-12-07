
from fractions import gcd



number,repeat=list(map(str,input().split()))  

digit=number[number.index(".")+1:]
interger=number[0:number.index(".")]
infinite=number[len(number)-int(repeat):]


mau=(10**(len(digit)-int(repeat)))*(10**(int(repeat))-1)

tu=int(interger+digit[0:int(len(digit)-int(repeat))])*((10**int(repeat))-1)+int(digit[len(digit)-int(repeat):])

a=gcd(tu,mau)

print(str(tu//a)+str("/")+str(mau//a))
