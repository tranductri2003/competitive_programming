from collections import defaultdict


class Solution(object):

    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        def check(a, b, c):

            if a[0] == b[0] or a[0] == c[0] or b[0] == c[0]:
                if a[0] == b[0] == c[0]:
                    return True
                else:
                    return False

            if a[1] == b[1] or a[1] == c[1] or b[1] == c[1]:
                if a[1] == b[1] == c[1]:
                    return True
                else:
                    return False

            if (b[1]-a[1])/(b[0]-a[0]) == (c[1]-a[1])/(c[0]-a[0]):
                return True
            return False

        visited = defaultdict(lambda: False)
        res = 0
        n = len(points)
        for i in range(n):
            for j in range(n):
                if visited[(i, j)] == False and visited[(j, i)] == False:
                    if j != i:
                        temp = 2
                        for k in range(n):
                            if k != i and k != j:
                                # print(i, j, k)
                                if check(points[i], points[j], points[k]):
                                    temp += 1
                        res = max(res, temp)
                        visited[(i, j)] = True
        if n == 1:
            return 1
        else:
            return res


t = Solution()
print(t.maxPoints([[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]))
# print(t.maxPoints([[1, 1], [1, 2], [1, 3], [3, 1], [4, 1], [5, 1], [6, 1]]))
