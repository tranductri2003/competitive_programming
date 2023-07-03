import math
import os
import random
import re
import sys


#
# Complete the 'isSpecialNumber' function below.
#
# The function is expected to return a BOOLEAN.
# The function accepts INTEGER number as parameter.
#


def getValidNumbers(s):
    res = []
    temp = ""
    for i in s:
        if i in "1234567890":
            temp += i
        else:
            if temp != "":
                res.append(int(temp))
            temp = ""
            pass
    temp = ""

    res.sort()
    ans = []
    for num in res:
        ans.append(str(num))

    ans = ", ".join(ans)
    return ans


print(getValidNumbers("ab123bx09aa222"))


# print(isSpecialNumber(n))
