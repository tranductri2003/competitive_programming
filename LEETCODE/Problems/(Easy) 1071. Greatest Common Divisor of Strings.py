class Solution(object):
    def gcdOfStrings(self, str1, str2):
        if str1+str2 != str2+str1:
            return ""
        else:
            from math import gcd
            return str1[:gcd(len(str1), len(str2))]

        #     if len(s) % len(temp) != 0:
        #         return False
        #     else:
        #         if s == (len(s)//len(temp))*temp:
        #             return True
        #         else:
        #             return False
        # for i in range(min(len(str1), len(str2)), -1, -1):
        #     if i == 0:
        #         return ""
        #     if check(str1, str1[:i]) and check(str2, str1[:i]):
        #         return str1[:i]
# class Solution(object):
#     def gcdOfStrings(self, str1, str2):
#         if(len(str1)==len(str2)):
#             if(str1==str2):
#                 return str1
#             else:
#                 return ""
#         while(len(str1)!=len(str2)):
#             if(len(str1)<len(str2)):
#                 if(str1==str2[:len(str1)]):
#                    str2=str2[len(str1):]
#                 else:
#                     return ""
#             else:
#                 if(str2==str1[:len(str2)]):
#                     str1=str1[len(str2):]
#                 else:
#                     return ""

#         if(str1==str2):
#             return str1
#         else:
#             return ""
