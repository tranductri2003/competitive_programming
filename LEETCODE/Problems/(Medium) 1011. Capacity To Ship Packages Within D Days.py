class Solution:
    def shipWithinDays(self, weights, days):
        l = max(weights)
        r = sum(weights)

        def check(capacity):
            curr = 0
            d = 1
            for i in weights:
                if curr+i > capacity:
                    d += 1
                    curr = 0
                curr += i
            if d > days:
                return False
            return True
        ans = 0
        while l <= r:
            mid = (l+r)//2
            if check(mid):
                ans = mid
                r = mid-1
            else:
                l = mid+1
        return ans
