def isSpecialNumber(number):
    i = 1
    temp = 0
    while True:
        temp += i
        if temp > number:
            return False
        elif temp == number:
            return True
        i += 1


n = int(input())
if isSpecialNumber(n):
    print("true")
else:
    print("false")
