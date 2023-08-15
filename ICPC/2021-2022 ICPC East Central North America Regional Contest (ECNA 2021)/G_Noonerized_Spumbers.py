s = list(input().split())
num1 = s[0]
num2 = s[2]
num3 = s[4]

n1 = len(num1)
n2 = len(num2)
n3 = len(num3)

# TH1: 1 va 2
for i in range(n1):
    for j in range(n2):
        tempNum1 = num1
        tempNum2 = num2

        tempNum1 = num2[:j+1] + num1[i+1:]
        tempNum2 = num1[:i+1] + num2[j+1:]

        if s[1] == "+":
            if int(tempNum1)+int(tempNum2) == int(num3):
                print(tempNum1, "+", tempNum2, "=", num3)
                quit()
        else:
            if int(tempNum1)*int(tempNum2) == int(num3):
                print(tempNum1, "*", tempNum2, "=", num3)
                quit()

# TH2: 1 va 3
for i in range(n1):
    for j in range(n3):
        tempNum1 = num1
        tempNum3 = num3

        tempNum1 = num3[:j+1] + num1[i+1:]
        tempNum3 = num1[:i+1] + num3[j+1:]

        if s[1] == "+":
            if int(tempNum1)+int(num2) == int(tempNum3):
                print(tempNum1, "+", num2, "=", tempNum3)
                quit()
        else:
            if int(tempNum1)*int(num2) == int(tempNum3):
                print(tempNum1, "*", num2, "=", tempNum3)
                quit()


# TH2: 2 va 3
for i in range(n2):
    for j in range(n3):
        tempNum2 = num2
        tempNum3 = num3

        tempNum2 = num3[:j+1] + num2[i+1:]
        tempNum3 = num2[:i+1] + num3[j+1:]

        if s[1] == "+":
            if int(num1)+int(tempNum2) == int(tempNum3):
                print(num1, "+", tempNum2, "=", tempNum3)
                quit()
        else:
            if int(num1)*int(tempNum2) == int(tempNum3):
                print(num1, "*", tempNum2, "=", tempNum3)
                quit()
