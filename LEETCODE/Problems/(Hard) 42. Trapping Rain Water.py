class Solution(object):
    def trap(self, height):
        n = len(height)
        left = [0]*n
        right = [0]*n

        current = height[0]
        for i in range(n):
            if height[i] > current:
                current = height[i]
            left[i] = current

        current = height[-1]
        for i in range(n-1, -1, -1):
            if height[i] > current:
                current = height[i]
            right[i] = current

        res = 0
        for i in range(n):
            res += min(left[i], right[i])-height[i]
        return res
