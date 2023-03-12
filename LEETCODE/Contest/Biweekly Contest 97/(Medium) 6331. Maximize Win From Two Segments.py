from collections import defaultdict
from bisect import bisect_right, bisect_left


class Solution(object):
    def maximizeWin(self, prizePositions, k):
        """
        :type prizePositions: List[int]
        :type k: int
        :rtype: int
        """
        distinct = list(set(prizePositions))
        check = defaultdict(lambda: -1)
        for num in prizePositions:
            check[num] += 1

        prefixSum = defaultdict(lambda: 0)
        prefixSum[0] = 0
        temp = 0
        for num in distinct:
            temp += check[num]
            prefixSum[num] = temp

        # Th1: 2k
        res1 = 0
        for i in range(0, len(distinct)):
            pre = distinct[i]
            post = bisect_left(distinct, distinct[i]+2*k)
            print(post)

        print(res1)

        #Th2: overlap
        res2 = 0
        data = []
        for i in range(1, len(distinct)):
            pre = distinct[i-1]
            post = distinct[bisect_right(distinct, distinct[i]+k)-1]
            data.append((prefixSum[post]-prefixSum[pre], [pre+1, post]))
        data.sort(key=lambda x: x[0], reverse=True)
        res2 += data[0][0]
        left = data[0][1][0]
        right = data[0][1][1]

        newData = [0]
        for i in range(1, len(distinct)):
            pre = distinct[i-1]
            post = distinct[bisect_right(distinct, distinct[i]+k)-1]
            print(pre+1, post)

            if pre+1 >= left and post <= right:
                print('1111')
                continue
            elif right >= post >= left:
                print('22222')
                post = distinct[bisect_right(distinct, left-1)-1]
                print(post)
            elif pre+1 <= right <= post:
                print("dcm")
                pre = distinct[bisect_left(distinct, right+1)]
                print(pre, post)
            newData.append(prefixSum[post]-prefixSum[pre])
            print(pre+1, post, newData)


t = Solution()
print(t.maximizeWin([1, 1, 2, 2, 3, 3, 5], 2))
