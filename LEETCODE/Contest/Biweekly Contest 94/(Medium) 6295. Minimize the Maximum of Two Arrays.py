from collections import defaultdict
import math


class Solution(object):
    def minimizeSet(self, divisor1, divisor2, uniqueCnt1, uniqueCnt2):
        """
        :type divisor1: int
        :type divisor2: int
        :type uniqueCnt1: int
        :type uniqueCnt2: int
        :rtype: int
        """
        # check = defaultdict(lambda: 0)
        # data1 = []
        # num1 = 0
        # i = 0
        # while num1 < uniqueCnt1:
        #     if check[i]==0 and i%divisor1!=0:
        #         data1
        if divisor1 == divisor2:
            maxSo1 = uniqueCnt1+uniqueCnt2
            loi1 = maxSo1//divisor1

            while loi1 != 0:
                maxSo1 += loi1
                loi1 //= divisor1
            return (maxSo1)
        else:
            maxSo1 = uniqueCnt1
            loi1 = maxSo1//divisor1

            while loi1 != 0:
                maxSo1 += loi1
                loi1 //= divisor1

            # target = uniqueCnt2//math.lcm(divisor1, divisor2)*math.lcm(divisor1, divisor2)
            # if
            # maxSo2 = uniqueCnt2
            # loi2 =
            # Lay lcm 2 div thi duoc lcm//div2
            soSoDuocChon = math.lcm(divisor1, divisor2) - \
                math.lcm(divisor1, divisor2)//divisor1-1
            if uniqueCnt2 % soSoDuocChon == 0:
                maxSo2 = (uniqueCnt2//soSoDuocChon-1) * \
                    math.lcm(divisor1, divisor2)+soSoDuocChon*divisor1-1
            else:
                print("as")
                print(soSoDuocChon)
                maxSo2 = (uniqueCnt2//soSoDuocChon)*math.lcm(divisor1,
                                                             divisor2)+(uniqueCnt2 % soSoDuocChon)*divisor1-1
            print(maxSo1, maxSo2)
            return max(maxSo1, maxSo2)


t = Solution()
print(t.minimizeSet(2, 7, 1, 3))
